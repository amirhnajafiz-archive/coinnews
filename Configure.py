# This file is the configure where it sends the data to repository we created
import subprocess
import shlex
import os
import datetime
from Tools.Directory import reset_path


# This function will send the data to repository branch that we choose
def push_to_repo(commit_date="nil"):
    if commit_date == "nil":  # getting the data if nothing entered
        commit_date = datetime.datetime.now().strftime("%b %d %Y")

    path = "./Setups/config"
    if os.path.exists(path):
        os.chdir("./Setups")
        with open("config", 'r') as file:
            repo_url = file.read()
            branch = file.read()
        subprocess.call(shlex.split(f'./run.sh {branch} {commit_date} {repo_url}'))
        reset_path()


# This function will setup a git repository in users system
def setup_git(url, branch):
    os.chdir("./Setups")
    subprocess.call(shlex.split(f'./git_set.sh {url} {branch}'))
    reset_path()


# This function checks the configuration exists
def is_config():
    return os.path.exists("./Setups/config")
