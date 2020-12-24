# This file sets the starting and finishing time of the program and creates directory names based on the date
import datetime


# This class is for getting the program executing time and define the file names and ...
class Set:
    def __init__(self):
        self.date_set = datetime.datetime.now()  # Clocks the running time of the script

    def get_time_string(self):  # Return the time in a format for user information
        return self.date_set.strftime("%A %d %B , %Y %H:%M:%S %z %Z")

    def get_dir_string(self):  # Return the time in a directory name format
        return self.date_set.strftime("%d%b%Y%Z")
