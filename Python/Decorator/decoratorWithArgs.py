def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                func(a)
        return wrapper  
    return decorator

@repeat(3)
def say_hello(a):
    print(f"Hello, {a}!")


say_hello("Dushyant")

'''
    It replaces the function say_hello with this :

    def decorator(func):
        def wrapper(a):
            for i in range(n):
                say_hello(a)
        return wrapper
'''



