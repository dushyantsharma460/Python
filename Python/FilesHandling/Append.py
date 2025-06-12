# As you now if file exist before as you write in python code it will clear the content of exsisting file.
# And replace the content with the new content you write in python code

# Append to a file called Mayank.txt
# It should add data about Mayank's Hometown

# This will add data to exsisting file not replace the data

f = open("Mayank.txt" , "a")

string = '''
Mayank initially lived in Sirsa(Hry.) and he start his graduation with in Sirsa's
College "The National College Sirsa" and now he was in undergraduation.
'''

# This will append the data at the end of the exsisting file

f.write(string)

f.close()