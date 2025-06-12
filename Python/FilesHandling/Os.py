import os

# d = os.listdir("dir")   # Try to run this is in Desktop/Python/Python/FileHandlings
# print(d)    # This will give the list of all the files and directory of dir


# d = os.listdir("Docstrings")    # Try to run this is in Desktop/Python/Python
# print(d)           # This will give the list of all the files and directory of Docstrings


# print(os.getcwd())      # give the path of current working directory 

print(os.path.exists("Docstrings"))    # print true if this file or directory is present in current path
#true -> Desktop/Python/Python            false -> Desktop/Python/Python/FileHandlings

print(os.path.exists("dir"))
#true -> Desktop/Python/Python/FileHandlings      false -> Desktop/Python/Python


# We can also remove the file by remove function

# os.remove("sample.txt")  # Desktop/Python/Python -> Give error    Desktop/Python/Python/FileHandlings -> Execute Easily 
# It ensure that the file will present in the same directory that you use to execute the code


# In os you can remove the file and you can remove only empty directory(no files include in that) by os 

# os.rmdir("dir")   # Show directory is not empty
os.rmdir("emptysdir")

# If you want to remove the non-empty directory we need to use the powerful module name (shutil)
