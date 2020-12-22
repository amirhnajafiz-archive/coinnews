# This file is the part where we create the files with their contents.
import random
import string
from file_types import Formatter


# A function to generate a random string with a specific length
def get_string(length):
    builder = ''
    while length > 0:
        remain = min(80, length)
        builder += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(remain))
        if remain == 80:
            builder += "\n"
        length -= 80
    return builder


# This functions creates a new file with its name and content and saves it
def generate_file(path, type_formatter, file_type="nil"):
    # File name
    name_length = 10
    file_name = get_string(name_length)
    # Content of the file
    content_length = 128
    content = get_string(content_length)
    content = type_formatter.get_start_comment(file_type) + "\n" + content + "\n" + type_formatter.get_end_comment(
        file_type)
    # Setting the directory name
    file_name = path + file_name + type_formatter.get_format(file_type)
    # Save into the created file
    with open(file_name, 'w') as file:
        file.write(content)
