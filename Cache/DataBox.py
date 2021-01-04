class Box:
    def __init__(self):
        self.file_number = 0
        self.commit_date = ""
        self.files_list = []

    @property
    def get_string(self):
        string = f'$${self.file_number}'
        string += f'$${self.commit_date}'
        string += f'$${self.files_list}'
        return string
