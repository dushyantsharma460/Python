# v1 - package 1 (pandas)
# v2 - package 2 (numpy)
# v3 - package 3 (moviepy)

# What if these packages keeps getting updated it is a pain
# My global package can only have a given version means that are on website of these packages respectively
# Now question is how do i freeze the version and we want to use different version numbers of the same package in different project
# Virtual environment solve this exact problem
# Create a isolated python environment for this project whatever i install in this python environment should not installed globally


# To create virtual environment use ->  pip install virtualenv 

# Set your first virtual environment -> python3 -m venv env1  ->  sudo apt install python3-venv (Ubuntu)
# From this env1 folder is created is in present directory

# If not working use this to proper installation -> python3 -m venv env1 

# To activate this we need -> source env1/bin/activate  (Ubuntu)  -> .\env\Scripts\Activate.ps1

# Now fresh start virtual environment is created -> previous installed library is not working
# Now pandas was install inide in virtual environment


# pip freeze -> Give all the packages with the version
# pip freeze > requirements.txt  -> Use this to install the file in your dir
# from above cmd it show i am taking output of pip freeze and writing it to the requirements.txt


# Now to deactivate the virtual environment  -> deactivate
# Now the part is to install the package one by one or use below cmd
# Copy the requirements.txt of to env2
# use this  ->  pip install -r requirements.txt
# (env2) -> It show you are in env2 virtual environment


# import moviepy 
# By running this cmd it show error because i am in (env2) moviepy is not installed in this as this is install in the global environment
# To make run this cmd you need to install moviepy in (env2)