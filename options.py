class Option:
    def __init__(self):
        self.files = []

    def initialize(self):
        try:
            index = 1
            with open("tools.txt", "r") as file:
                self.files = [f"{index}.{line.strip()}" for line in file.readlines()]
                index += 1
        except FileNotFoundError as error:
            print(error)

    def get_file(self, index):
        return self.files[index]

    def view_list(self):
        print(*self.files, sep="    |    ")
