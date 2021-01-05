# This file is our console base script to communicate with user from terminal
from Committer import program_setups_check, execute, push_message
from Cache.Cacher import cache_init, cache_in, cache_clear


# This function creates a line break with "#"
def get_line_break():
    string = "\n"
    for i in range(50):
        string += "#"
    return string + "\n"


# Starting massage for our application
def input_massage():
    string = "> Enter your commands like :"
    string += "\n" + "   new  => for executing the committer builder."
    string += "\n" + "   quit => for exiting the program."
    string += "\n" + "  cache => for seeing the history of committer builds."
    string += "\n" + "  clear => for deleting the cache history."
    return string


# Ending massage in our application
def exit_massage():
    return "< ! Committer terminated >"


def cache_output():
    print(get_line_break())
    print("Program cache view :")
    cache_list = cache_in()
    if cache_list:
        for item in cache_list.keys():
            print(f'> {item}. Number of files {cache_list[item][0]}, files indexes {cache_list[item][1]}')
    else:
        print("> Cache is empty.")


def empty_cache():
    cache_clear()
    print(get_line_break())
    print("> Cache is now empty.")

# Initializing function of console
def init():
    cache_init()
    print(">>> Committer started ...")
    program_setups_check()
    print(get_line_break())


# Main method of the console script
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
        elif order == "cache":
            cache_output()
        elif order == "clear":
            empty_cache()
        else:
            print("> Not valid.")
        print(get_line_break())


# Program starts
if __name__ == "__main__":
    start_console()
    print(get_line_break() + "\n" + exit_massage())
