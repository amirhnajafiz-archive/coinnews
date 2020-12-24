# In this file we only have the methods for checking the existence of the directories.
import os


# This function corrects the path to documents
def correct_path():
    os.chdir("./Tools")


# This functions resets the path from documents
def reset_path():
    current_pace = os.getcwd()
    path_dir = os.path.dirname(current_pace)
    os.chdir(path_dir)


# This function checks if the directory that we work on is exist
def dir_init(path="./Documents"):
    if not os.path.exists(path):
        os.mkdir(path)


# This function checks the directory existence inside the documents
def dir_search(path="Empty"):
    if path == "Empty":
        return False
    else:
        dir_init("./Documents/" + path)
        return True
