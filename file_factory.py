from dir_check import dir_init, in_doc_search
from file_maker import generate_file
from part_time import Set
from options import Option


# This method checks the directories status for existence
# Returns a new Set instance
def initialize():
    dir_init()
    temp = Set()
    in_doc_search(temp.get_dir_string())
    return temp


# This method creates the files for user
def make_files(total_number, time_setter, file_type):
    for i in range(total_number):
        file_path = "./Documents/"+time_setter.get_dir_string()+"/"
        generate_file(file_path, file_type)
    print(f"{time_setter.get_time_string()}\nNew file added")


# Script execute method
def execute():
    number = input("Number >> ")
    option_view = Option()
    option_view.initialize()
    option_view.view_list()
    file_format = input("Type >> ")
    setter = initialize()
    make_files(int(number), setter, file_format)


if __name__ == "__main__":
    execute()
