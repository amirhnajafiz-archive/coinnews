# Formatter class manages the file types and their comments types
class Formatter:
    def __init__(self):
        # List of the file types we support
        self.type_list = {
            "python": ".py",
            "javascript": ".js",
            "c++": ".cpp",
            "c": ".c"
        }

    @staticmethod
    def get_start_comment(input_type="nil"):  # A method for getting the starting comment order
        if input_type == "python":
            return "\"\"\""
        elif input_type == "javascript" or input_type == "c++" or input_type == "c":
            return "/*"
        else:
            return " "

    @staticmethod
    def get_end_comment(input_type="nil"):  # A method for getting the finishing comment order
        if input_type == "python":
            return "\"\"\""
        elif input_type == "javascript" or input_type == "c++" or input_type == "c":
            return "*/"
        else:
            return " "

    def get_format(self, input_type="nil"):  # A method for getting the file format of a language
        if input_type in self.type_list.keys():
            return self.type_list.get(input_type)
        else:
            return ".txt"
