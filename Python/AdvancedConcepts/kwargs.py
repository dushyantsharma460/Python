def marks(**kwargs):       #kwargs gives dictionary 
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")


marks(dushyant = 59, mayank = 63, divyansh = 61)