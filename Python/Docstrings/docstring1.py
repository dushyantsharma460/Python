def add(a, b):
    '''Returns the sum of two numbers.'''
    return a + b


print(add.__doc__)   # Output: Returns the sum of two numbers.


# __doc__   
# Docstring looks like a regular python comment but if you write it right after the function this is called docstring 
# Python have design docstring because sometime we want to attach information to function like what parameter it is accept and what return
# Any information that you want to add to python function whenever user hover on it