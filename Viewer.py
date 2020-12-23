# This class is for showing user , the program options so the user chooses the file types from what we define
class Option:
    def __init__(self):  # Constructor
        self.files = []
        self.format_files = []

    def format_init(self):  # Create a formatted type from files
        index = 1
        for file in self.files:
            self.format_files.append(f"{index}.{file}")
            index += 1

    def get_file(self, index):  # Get the list of the files we support
        return self.files[index]

    def view_list(self):  # Printing the list of the files we support
        print(*self.format_files, sep="    |    ")
