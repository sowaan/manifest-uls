from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue

# Define the insert_data function outside of the class

def insert_data(arrays, frm, to):
    shipment_num = None
    
    for line in arrays:
        # Extract the doctype name using slicing (assuming the name is at index 45-50)
        doctype_name = "R" + line[frm:to].strip()
        
        
        try:
            # Fetch the definition document based on the extracted doctype name
            definition = frappe.get_doc("Definition Manifest", doctype_name)
            for row in definition.definitions:
                if row.field_name == "shipment_number":
                    shipst=row.from_index-1
                    shipto=row.to_index
                    shipment_num = line[shipst:shipto].strip()
                    break
        except frappe.DoesNotExistError:
            # If doctype_name doesn't exist in Definitions, move to the next line
            continue

        docs = frappe.get_list(doctype_name, filters={'shipment_number': shipment_num})
        if docs :
            docss = frappe.get_doc(doctype_name , docs[0])
            for child_record in definition.definitions:
                field_name = child_record.field_name
                from_index = child_record.from_index - 1
                to_index = child_record.to_index
                # Search and extract field_data from line using from_index and to_index
                field_data = line[from_index:to_index].strip()
                docss.set(field_name, field_data)
            docss.save()
            frappe.db.commit()
            print(doctype_name, shipment_num, "Updating")
                
        
        else:
            
                doc = frappe.new_doc(doctype_name)
                
                # Iterate over each child record
                for child_record in definition.definitions:
                    field_name = child_record.field_name
                    from_index = child_record.from_index -1
                    to_index = child_record.to_index
                    # Search and extract field_data from line using from_index and to_index
                    field_data = line[from_index:to_index].strip()
                    # Set the field data in the document
                    doc.set(field_name, field_data)
                    
                # Save the new document
                print(doctype_name , shipment_num,"Inserting")
                doc.insert()
                doc.save()
            

class ManifestUploadData(Document):
    def on_submit(self):
       
        if self.attach_file:
            
            # Get the name of the file attached to the document
            file_name = frappe.db.get_value("File", {"file_url": self.attach_file}, "name")
            # Get the content of the attached file
            file_doc = frappe.get_doc("File", file_name)
            content = file_doc.get_content()
            arrays = content.split('\n')
            frm = int(self.from_index)-1
            to = int(self.to_index)
            chunk_size = 10  # Number of lines per chunk
            current_index = 0  # Starting index for slicing the array

            # Continue processing chunks until all lines are processed
            while current_index < len(arrays):
                # Take the next chunk of lines
                chunk = arrays[current_index:current_index + chunk_size]                
                # Update the current index for the next chunk
                current_index += chunk_size
                enqueue(insert_data, arrays=chunk,frm=frm, to=to, queue="default")
            # insert_data( arrays,frm, to)