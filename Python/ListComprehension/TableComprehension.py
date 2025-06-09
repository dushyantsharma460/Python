#Simple 

table = []

for i in range(1,11):
    table.append(5 * i)


#By using list comprehension 

table = [f"5 * {i} = {5*i}" for i in range(1, 11)]

for ele in table:
    print(ele)
