class Option:
    def __init__(self):
        self.files = []
        self.format_files = []

    def initialize(self):
        try:
            with open("tools.txt", "r") as file:
                self.files = [line.strip() for line in file.readlines()]
        except FileNotFoundError as error:
            print(error)

    def format_init(self):
        index = 1
        for file in self.files:
            self.format_files.append(f"{index}.{file}")
            index += 1

    def get_file(self, index):
        return self.files[index]

    def view_list(self):
        print(*self.format_files, sep="    |    ")
