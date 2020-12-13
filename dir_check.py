import os


# This function checks if the directory that we work on is exist
def dir_init():
    path = "./Documents"
    if not os.path.exists(path):
        os.mkdir(path)
