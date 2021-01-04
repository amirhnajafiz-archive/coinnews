import os
import datetime


local_path = "record.data"


def cache_init():
    if not os.path.exists(local_path):
        with open(local_path, "w") as file:
            file.writelines([f'$Cache Created : {datetime.datetime.now()}'])


def cache_up(box):
    with open(local_path, "r") as file:
        lines = file.readlines()
    with open(local_path, "w") as file:
        file.writelines(lines)
        file.write(f'\n&$${box.file_number}$${box.files_list}')


def cache_in():
    with open(local_path, "r") as file:
        lines = file.readlines()
        new_lines = [line for line in lines if line.startswith("&")]
    return new_lines


def cache_clear():
    with open(local_path, "w") as file:
        file.writelines([f'$Cache Created : {datetime.datetime.now()}'])
