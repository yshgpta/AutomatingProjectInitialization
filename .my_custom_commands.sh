#!/bin/bash


# Change the function name to give custom name to your command. Initially it is: create Your_Repo_Name Your_user_name Your_password

function create() {
	cd ~
	python create.py $1 $2 $3   #If you want to give only the repo_name i.e. like create Your_Repo_Name then just delete the $2 $3 and provide username and password in create.py
	cd /home/yshgpta/Desktop/MyProjects/$1   #Change the path to your own project folder path
	git init
	git remote add origin http://github.com/yshgpta/$1.git  #Change the username to your own github username
	touch README.md
	git add .
	git commit -m "Initial Commit"
	git push origin master
	code .
}
  
