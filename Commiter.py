# This is our program main file which will connect the application part together
from Tools.Builder import execute
from Configure import push_to_repo, setup_git, is_config


if __name__ == "__main__":
    execute()
    push_to_repo()
