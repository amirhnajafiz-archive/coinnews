#!/usr/bin/bash

# Data will be send with a date and a branch name to the repository we have

# Checking in the branch user wants
git checkout "$5"

# Performing a commit to the date of the user
git add .
git commit --amend --no-edit --date="$1 $2 $3"

xdotool key "control+x"
git pull --allow-unrelated-histories "$4"
# Put this in instaltion tool kit
# apt install xdotool

git push -u origin "$5"
