def funcGenerator(func):
    def newfunc():
        print("Hey I am the new function first line")
        func()
        print("Hey I am the new function last line")
    return newfunc

@funcGenerator        # Changing the function forever according to newfunc
def original_function():
    print("I am the original function")      # Decorator is used to change the functionality of existing function

# f = funcGenerator(original_function)
# f()

original_function()
