from Committer import program_setups_check, execute, push_message
import os


def get_line_break():
    string = ""
    for i in range(os.get_terminal_size().columns):
        string += "#"
    return string


def init():
    print(">>> Committer started ...")
    program_setups_check()
    print(get_line_break())
