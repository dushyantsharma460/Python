# The walrus operator := (introduced in Python 3.8) is used for assignment expressions — allowing you to assign and use a variable in a single expression.

def double():
    print("thinking...")
    print("designing...")
    print("coding...")
    print("using...")
    return 70

if(double() > 7):
    double()
else:
    print("Not Greater than 7")



# a = double() 
# if(a > 7):
#     print(a)
# else:
#     print("Not Greater than 7")


# Now getting the value with walrus
# Example 1 ->

if((a:= double() > 7)):
    print(a)

else:
    print("Not Greater than 7")


# Example 2 ->

while(data := input("Enter the value :")):
    print(data)
    if data == "q":
        break


# Example 3 ->

# Without walrus
line = input("Enter a line: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter a line: ")

# With walrus
while (line := input("Enter a line: ")) != "quit":
    print(f"You entered: {line}")


# Example 4 ->
# Avoid calling len() twice
data = [1, 2, 3, 4, 5]

if (n := len(data)) > 3:
    print(f"List is long ({n} elements)")
