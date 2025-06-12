# f = open("Dushyant.txt", "rt")   # Read this file in text mode
f = open("Dushyant.txt", "r")    # By default it read the text file no need to write rt
# f = open("Dushyant.txt", "rb")    # This is used to read binary files

content = f.read()

print(content)

f.close()