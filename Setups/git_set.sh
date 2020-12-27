#!/usr/bin/bash

# Setting up the git repository
echo "Enter your repository url : "
read -e repourl

echo "Enter your branch name : "
read -e branchname

# Initialize
git init
git clone "$repourl"

# Creating the gitignore file
echo "git_set.sh" > .gitignore

# Add a remote
git remote add origin "$repourl"

git add .
git commit -m "Startup"

# Add files to base
git push -u origin master

# Create a pull request
xdotool key "control+x"
git pull --allow-unrelated-histories "$repourl"

# Add a new branch
git checkout -b "$branchname"

echo $(date) + " Repo created successfully." > config

# Adding files to new branch
git add .
git commit -m "Start branch"

# Sending the config file into repo
git push -u origin "$branchname"

git checkout master
