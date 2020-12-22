# Formatter class manages the file types and their comments types
class Formatter:
    def __init__(self):
        # List of the file types we support
        self.type_list = {}
        self.files_initialize()

    def get_start_comment(self, input_type="nil"):  # A method for getting the starting comment order
        if input_type in self.type_list.keys():
            return self.type_list.get(input_type)[1]
        else:
            return " "

    def get_end_comment(self, input_type="nil"):  # A method for getting the finishing comment order
        if input_type in self.type_list.keys():
            return self.type_list.get(input_type)[1]
        else:
            return " "

    def get_format(self, input_type="nil"):  # A method for getting the file format of a language
        if input_type in self.type_list.keys():
            return self.type_list.get(input_type)[0]
        else:
            return ".txt"

    def get_files_list(self):
        return list(self.type_list.keys())

    def files_initialize(self):
        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split(":")
                self.type_list[parts[0].strip()] = []
                self.type_list[parts[0].strip()].append(parts[1].strip())
                self.type_list[parts[0].strip()].append(parts[2].strip())
                self.type_list[parts[0].strip()].append(parts[3].strip())
