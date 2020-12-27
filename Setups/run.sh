#!/usr/bin/bash

# Getting the date from user
echo "Enter your date : "
date_time=$(date)
read -e date_time

# Performing a commit to the date of the user
git add .
git commit --amend --no-edit --date="$date_time"

xdotool key "control+x"
git pull --allow-unrelated-histories "https://github.com/Official21A/CommiterTestBench.git"
# Put this in instaltion tool kit
# apt install xdotool

git push -u origin master
