from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in manifest_data/__init__.py
from manifest_data import __version__ as version

setup(
	name="manifest_data",
	version=version,
	description="Manifest Data is a custom ERPNext application designed to streamline the process of uploading and managing data from text files into ERPNext. With Manifest Data, users can effortlessly upload text files containing structured data, and the application automatically parses and inserts the data into designated doctypes and their corresponding fields within the ERPNext instance. This application simplifies the data import process, saving time and reducing the risk of errors associated with manual data entry. Whether it\'s importing customer information, inventory data, or any other type of data, Manifest Data offers a seamless solution for efficiently populating ERPNext with external data sources.",
	author="fariz.khanzada@sowaan.com",
	author_email="fariz.khanzada@sowaan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
