# This file is the base of our script which creates the files, manages the directories, all classes and ....
from Tools.Directory import dir_init, dir_search
from Tools.FileMaker import generate_file
from Tools.TypeManage import Formatter
from Tools.Timer import Set
from Tools.Viewer import Option
from Cache.DataBox import Box
from Cache.Cacher import cache_init, cache_up


# This method checks the directories status for existence.
# Returns a new Set instance.
def initialize():
    cache_init()
    dir_init()
    temp = Set()
    dir_search(temp.get_dir_string())
    return temp


# This method creates the files for user.
def make_files(total_number, time_setter, formatter, file_type):
    for i in range(total_number):
        file_path = "./Documents/"+time_setter.get_dir_string()+"/"
        generate_file(file_path, formatter, file_type)
    print(f"> {time_setter.get_time_string()} New files added.")


# This method creates a view and returns it.
def present_view(formatter):
    option_view = Option()
    option_view.files = formatter.get_files_list()
    option_view.format_init()
    return option_view


# In this method we split the use command line input to takeout the indexes.
def input_line_break(string_line, option_view):
    numbers = [int(num.strip()) for num in string_line.split(" ")]
    files_list = [option_view.get_file(num-1) for num in numbers]
    return files_list


# Script execute method.
def execute():
    data_box = Box
    number = input("> (How many files) $ ")
    data_box.file_number = number
    type_formatter = Formatter()  # See TypeManage.py
    # Creating viewer
    option_viewer = present_view(type_formatter)
    option_viewer.view_list()
    # Input command line
    file_format = input("> (Programming language index/indexes) $ ")
    data_box.files_list = file_format
    format_list = input_line_break(file_format, option_viewer)
    # Program setter
    setter = initialize()
    # File creating
    for type_file in format_list:
        make_files(int(number), setter, type_formatter, type_file)
    cache_up(data_box)
