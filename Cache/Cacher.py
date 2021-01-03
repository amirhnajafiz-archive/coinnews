import os
import datetime


def cache_init():
    if not os.path.exists("/Cache/record.data"):
        with open("/Cache/record.data", "w") as file:
            file.writelines([f'$Cache Created : {datetime.datetime.now()}'])
