# Write to a file called Mayank.txt
# It should contain data about Mayank

f = open("Mayank.txt" , "w")   # By default it write to text file and if you want to write in binary file use wb

string = '''
Mayank is nice guy . He lives in Sirsa and he works on tally software .
His hobby is going GYM daily.
'''

f.write(string)

f.close()

# When you run this code this create automatically a new file Mayank.txt with the content that you write