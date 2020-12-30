# This is our program main file which will connect the application part together
from Tools.Builder import execute
from Configure import push_to_repo, setup_git, is_config


# This function will setup the basics if needed
def program_setups_check():
    if not is_config():
        url = input("Please enter the git url >> ")
        branch = input("Please enter the name of the branch >> ")
        setup_git(url, branch)
    else:
        print("<< Everything is OK, welcome to the committer >>")


# This function will get the commit date from user
def get_date_from_user():
    return input("Please enter your date (or type nil for today date) >> ")


# This function asks the user before push the changes into the repository
def push_message():
    cmd = input("Do you want to push to repository right now ? ( y / N )  >> ")
    if cmd == "y":
        push_to_repo(commit_date=get_date_from_user())
    else:
        print("Your files are saved in \'Documents\'")


# Program starts
if __name__ == "__main__":
    program_setups_check()  # git checkup
    execute()  # Script execute
    push_message()  # Upload on git
