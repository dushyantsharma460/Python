# Map Example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square_list = list(map(lambda a: a**2, numbers))         # Needs to convert it into list

print(Square_list)


#Filter Example

Less_Than_36_List = list(filter(lambda x : x < 36 ,Square_list))     # Needs to convert it into list
print(Less_Than_36_List)


# Reduce Example 

# To use reduce you need to import first

from functools import reduce

Sum_of_first_10 = reduce(lambda a ,b: a + b ,numbers)

print(Sum_of_first_10)