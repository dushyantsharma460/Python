# Creating Command Line Utilities as in java....(Which take input from command)

# Send argument in file        Ex: python3 argparse.py 4 8 add
# Make like this program add these two number when these argument pass to the file
# But at this time argparse.py is not ready to take 4,8 and add 

import argparse
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1", type = float , help = "First Number")
parser.add_argument("num2", type = float , help = "Second Number")
parser.add_argument("operation", choices=["add","sub" ,"mul" ,"div"], help="Operation to perform")

args = parser.parse_args()

print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print("Some error Occured")