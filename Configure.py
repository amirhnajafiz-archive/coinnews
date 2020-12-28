import subprocess
import shlex
import os
import datetime
from Tools.Directory import reset_path


def push_to_repo(commit_date="nil"):
    if commit_date == "nil":
        commit_date = datetime.datetime.now().strftime("%b %d %Y")

    path = "./Setups/config"
    if os.path.exists(path):
        os.chdir("./Setups")
        with open("config", 'r') as file:
            repo_url = file.read()
            branch = file.read()
        subprocess.call(shlex.split(f'./run.sh {branch} {commit_date} {repo_url}'))
        reset_path()
