# This file is our console base script to communicate with user from terminal
from Committer import program_setups_check, execute, push_message, execute_from_cache, get_types
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
    string += "\n" + "  rerun => for executing old commands."
    string += "\n" + "   quit => for exiting the program."
    string += "\n" + "  cache => for seeing the history of committer builds."
    string += "\n" + "  clear => for deleting the cache history."
    return string


# Ending massage in our application
def exit_massage():
    return "< ! Committer terminated >"


# This method gets the cache data from "Cacher" and prints it into the console
def cache_output():
    print(get_line_break())
    print("Program cache view :")
    cache_list = cache_in()
    if cache_list:
        for item in cache_list.keys():
            files_names = get_types(cache_list[item][1])
            print(f'> {item}. Number of files {cache_list[item][0]}, files   ', end='')
            print(*files_names, sep="  |  ")
    else:
        print("> Cache is empty.")
    return len(cache_list)


# This method will call the "cache clear" method to empty the cache.
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


# This method allows the user to execute the old commands again
def run_by_cache():
    out_result = cache_output()
    if out_result == 0:
        return
    index_list = input("\n> (Enter the cache indexes) $ ")
    chosen_list = [index for index in index_list.split(" ")]
    cache_list = cache_in()
    for index in chosen_list:
        try:
            file_index_string_line = " ".join(map(str, cache_list[index][1]))
            execute_from_cache(cache_list[index][0], file_index_string_line)
        except IndexError:
            print("\n>>> Cache has a problem, we suggest you to clear cache ones. This might caused by bad request.\n")
        except KeyError:
            print("\n>>> Cache is empty, or the key you entered is not in cache items.\n")
    push_message()


# Main method of the console script
def start_console():
    init()
    print(input_massage())
    try:
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
            elif order == "rerun":
                run_by_cache()
            else:
                print("> Not valid.")
            print(get_line_break())
    except (KeyboardInterrupt, EnvironmentError):
        print(get_line_break())
        print("> Program terminated in a bad way !")


# Program starts
if __name__ == "__main__":
    start_console()
    print(get_line_break() + "\n" + exit_massage())
