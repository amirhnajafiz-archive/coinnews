from Committer import program_setups_check, execute, push_message
import os


def get_line_break():
    string = "\n"
    for i in range(50):
        string += "#"
    return string + "\n"


def input_massage():
    string = "> Enter your commands like :"
    string += "\n" + "  new  => for executing the committer builder."
    string += "\n" + "  quit => for exiting the program"
    return string


def exit_massage():
    return "< ! Committer terminated >"


def init():
    print(">>> Committer started ...")
    program_setups_check()
    print(get_line_break())


def start_console():
    init()
    print(input_massage())
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


if __name__ == "__main__":
    start_console()
    print(get_line_break() + "\n" + exit_massage())
