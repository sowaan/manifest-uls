from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue

# Define the insert_data function outside of the class
def insert_data(arrays, frm, to):
    for line in arrays:
        # Extract the doctype name using slicing (assuming the name is at index 45-50)
        doctype_name = "R" + line[frm:to].strip()
        shipment_num = line[33:44].strip()
        
        try:
            # Fetch the definition document based on the extracted doctype name
            definition = frappe.get_doc("Definition Manifest", doctype_name)
        except frappe.DoesNotExistError:
            # If doctype_name doesn't exist in Definitions, move to the next line
            continue

        # Create a new document for the current doctype

        ex = frappe.db.exists(doctype_name , shipment_num)
        if ex:
            doc = frappe.get_doc(doctype_name, shipment_num)
            print(definition,"definitions","Updating",shipment_num)
            for child_record in definition.definitions:
                field_name = child_record.field_name
                from_index = child_record.from_index - 1
                to_index = child_record.to_index
                # Search and extract field_data from line using from_index and to_index
                field_data = line[from_index:to_index].strip()
                doc.set(field_name, field_data)
                doc.save()
                frappe.db.commit()
        
        else:
            doc = frappe.new_doc(doctype_name)
            print(definition,"definitions","Uploading",shipment_num)
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
            # insert_data( arrays,frm, to)
            enqueue(insert_data, arrays=arrays,frm=frm, to=to, queue="default")
            
