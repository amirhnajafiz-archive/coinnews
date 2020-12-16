from dir_check import dir_init, in_doc_search
from file_maker import generate_file
from part_time import Set


# This method checks the directories status for existence
# Returns a new Set instance
def initialize():
    dir_init()
    temp = Set()
    in_doc_search(temp.get_dir_string())
    return temp


# This method creates the files for user
def make_files(total_number, time_setter):
    for i in range(total_number):
        file_path = "./Documents/"+time_setter.get_dir_string()+"/"
        generate_file(file_path, "javascript")
    print(f"{time_setter.get_time_string()}\nNew file added")


# Script execute method
def execute():
    number = input(">> ")
    setter = initialize()
    make_files(int(number), setter)


if __name__ == "__main__":
    execute()