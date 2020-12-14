import os


# This function checks if the directory that we work on is exist
def dir_init(path="./Documents"):
    if not os.path.exists(path):
        os.mkdir(path)


# This function checks the directory existence inside the documents
def in_doc_search(path="Empty"):
    if path == "Empty":
        return False
    else:
        dir_init("./Documents/"+path)
        return True
