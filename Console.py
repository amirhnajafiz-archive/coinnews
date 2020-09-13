from Committer import program_setups_check, execute, push_message
import os


def get_line_break():
    string = ""
    for i in range(os.get_terminal_size().columns):
        string += "#"
    return string


def input_massage():
    string = "> Enter your commands like : $ <command>"
    string += "\n" + "  -- new  => for executing the committer builder."
    string += "\n" + "  -- quit => for exiting the program"


def init():
    print(">>> Committer started ...")
    program_setups_check()
    print(get_line_break())


def start_console():
    init()
    input_massage()
    while True:
        order = input("$ ")
        order = order.strip()
        if order == "quit":
            break
        elif order == "new":
            execute()
            push_message()
        else:
            print("> Not valid.")
        print(get_line_break())

