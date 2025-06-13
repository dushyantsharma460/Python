try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("What kind of operation do you want to perform.\nPress '+' for addition \nPress '-' for subtraction \nPress '*' for multiplication \nPress '/' for division")
    o = input("Enter Operation: ")

    match o:
        case '+':
            print(f"The result of a + b is {a + b}")
        case '-':
            print(f"The result of a - b is {a - b}")
        case '*':
            print(f"The result of a * b is {a * b}")
        case '/':
            if b == 0:
                print("Cannot divide by zero")
            else:
                print(f"The result of a / b is {a / b}")
        case _:
            print("Invalid operation")

except ValueError:
    print("Enter a valid integer for a and b")
