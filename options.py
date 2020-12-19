class Option:
    def __init__(self):
        self.files = []

    def initialize(self):
        try:
            with open("tools.txt", "r") as file:
                self.files = [line.strip() for line in file.readlines()]
        except FileNotFoundError as error:
            print(error)

    def get_file(self, index):
        return self.files[index]

    def view_list(self):
        print(*self.files, sep=" | ")
