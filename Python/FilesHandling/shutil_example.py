# Shutil module is very similar to os module but the difference is that shutil module is bit powerful
# Shutil can delete your file as well as directory



# import shutil

# shutil.rmtree("dir")     # delete all the file include directory dir

# You have to very very careful before running this type of program because this can actually clear your directory
# It is very powerful module for this reson 


# You can always copy a file using shutil


# shutil.copy("source.txt", "destination.txt")



import os

print(os.path.exists("source.txt")) 


import shutil

source = "source.txt"
destination = "destination.txt"

shutil.copy(source, destination)
print("File copied successfully.")

shutil.copy("destination.txt", "des2.txt")


# First it take the file which is move and then in second argument it take destination

shutil.move("des2.txt", "dir/")             # Move this file to dir/
