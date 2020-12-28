#!/usr/bin/bash

# Checking in the branch user wants
git checkout $1

# Performing a commit to the date of the user
git add .
git commit --amend --no-edit --date="$2"

xdotool key "control+x"
git pull --allow-unrelated-histories "$3"
# Put this in instaltion tool kit
# apt install xdotool

git push -u origin $1
