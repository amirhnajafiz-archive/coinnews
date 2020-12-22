# This file sets the starting and finishing time of the program and creates directory names based on the date
import datetime


# This class is for getting the program executing time and define the file names and ...
class Set:
    def __init__(self):
        self.date_set = datetime.datetime.now()

    def get_time_string(self):
        return self.date_set.strftime("%A %d %B , %Y %H:%M:%S %z %Z")

    def get_dir_string(self):
        return self.date_set.strftime("%d%b%Y%Z")
