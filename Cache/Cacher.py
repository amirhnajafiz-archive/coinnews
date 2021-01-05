# This part is our cacher file, where the history of the user inputs will be saved into a file.
import os
import datetime


local_path = "record.data"  # Path of the cache file.


# This method created the cache data file
def cache_init():
    if not os.path.exists(local_path):
        with open(local_path, "w") as file:
            file.writelines([f'$._Cache Created : {datetime.datetime.now()}'])


# In this method we add a new order to cache data
def cache_up(box):
    with open(local_path, "r") as file:
        lines = file.readlines()
    with open(local_path, "w") as file:
        file.writelines(lines)
        file.write(f'\n&._${box.file_number}_${box.files_list}_$#')


# This methods returns what ever is packed into cache data file
def cache_in():
    cache_lines = {}
    with open(local_path, "r") as file:
        lines = file.readlines()
        index = 0
        for line in lines:
            if line.startswith("$"):
                continue
            parts = line.strip().split("_$")
            total_number = int(parts[1])
            files = parts[2].split(" ")
            files = [int(number) for number in files]
            cache_lines[str(index)] = (total_number, files)
            index += 1
    return cache_lines


# This method empties the cache.
def cache_clear():
    with open(local_path, "w") as file:
        file.writelines([f'$._Cache Created : {datetime.datetime.now()}'])
