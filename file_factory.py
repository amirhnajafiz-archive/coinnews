from dir_check import dir_init
from file_maker import generate_file


def initialize(total_number):
    dir_init()
    for i in range(total_number):
        generate_file()
        print("New file added")


number = input(">> ")
initialize(int(number))
