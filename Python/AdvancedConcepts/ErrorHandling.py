# Try and except statement are used to hangle error in python
# We can wrap our program inside try and except they were take care of the error
# Whenever the error the code inside the except block is ran
# If there is no error try block keep execute normally
# Whenever the error inside try except block is executing and program does't crash


# Handle different error differently
# while True:
#     try: 
#         a = int(input("Enter the first number 1: "))
#         b = int(input("Enter the second number 2: "))

#         print("The division is", a / b)

#     # except:
#     #     print("Some Error Occureed !")

#     except ValueError:
#         print("Please don't perform bad typecasts")

#     except ZeroDivisionError:
#         print("Hey don't divide by 0")

#     except Exception as e:              # Printing the error by e
#         print("Error Occureed !", e)



# Raising the error
# When we wants to stop user for to tell them this is not required or don't make sense in my code
# In this case we hold the user and tell somthing is wrong with your side let's stop your execution
# Now we throw custom error

a = int(input("Enter the first number 1: "))
b = int(input("Enter the second number 2: "))

if b==0:
    raise ValueError("Please don't divide by 0")

print("The division is", a / b)
