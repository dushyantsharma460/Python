# Sum of variable arguments

def sum(*args):
    print(args)   # args will be a tuple of all the values passed to sum
    t = 0
    for item in args:
        t += item
    return t

print(sum(3,5,7,3,6,4))


