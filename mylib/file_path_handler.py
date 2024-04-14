import os
import json

class FilePathHandler:
    def __init__(self, data_folder="data", mylib_folder="mylib", config_file="config.json", doc_links_file="links.json", contacts_file="contacts.json"):
        self.current_directory = os.getcwd()
        self.data_directory = os.path.join(self.current_directory, data_folder)
        self.file_paths = self.get_file_paths()
        self.file_names = self.get_file_names()
        self.config_file_path = os.path.join(self.current_directory, mylib_folder, config_file)
        self.doc_links_file_path = os.path.join(self.current_directory, data_folder, doc_links_file)
        self.contacts_file_path = os.path.join(self.current_directory, data_folder, contacts_file)
        self.doc_links = self.read_doc_links()
        self.contact_names = self.read_contact_names()

    def get_file_paths(self):
        return [os.path.join(self.data_directory, filename) for filename in os.listdir(self.data_directory) if filename.endswith(".txt")]

    def get_file_names(self):
        return [os.path.splitext(os.path.basename(file_path))[0] for file_path in self.file_paths]

    def read_doc_links(self):
        with open(self.doc_links_file_path, "r") as json_file:
            return json.load(json_file)

    def read_contact_names(self):
        with open(self.contacts_file_path, "r") as json_file:
            return json.load(json_file)
