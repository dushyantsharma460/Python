# By Handling error by else block

'''
try:
    a = 848/0

except Exception as e:
    print(e)

# Get executed when there is no error in the try block
else:
    print("Code is well")

'''

# Finally Keyword

'''
a = int(input("Enter the first number 1: "))
b = int(input("Enter the second number 2: "))

try: 
    c = a / b 
    print(c)

except Exception as e:
    print(e)

# This is always executed no matter if try completely executed or not
finally:
    print("This is always executed")

# print("This is always executed")  # If this always excuted so this statement is always executed

'''




# Now question is what the benifit of finally
# Finally is mainly use in fuction that return something 

def divide(a,b):
    try:
        c = a / b
        print(c)
        return c
    
    except Exception as e:
        print(e)
        return None
    
    finally:
        print("This is always executed")

a = int(input("Enter the first number 1: "))
b = int(input("Enter the second number 2: "))
divide(a,b)