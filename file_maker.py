import random
import string


# A function to generate a random string with a specific length
def get_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


# File name
name_length = 10
file_name = get_string(name_length)
# Content of the file
content_length = 128
content = get_string(content_length)

# Save into the created file
with open(file_name, 'w') as file:
    file.write(content)
