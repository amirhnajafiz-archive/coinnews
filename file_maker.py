import random
import string


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


# File name
name_length = 10
file_name = get_string(name_length)
# Content of the file
content_length = 128
content = get_string(content_length)

# Save into the created file
with open(file_name, 'w') as file:
    file.write(content)
