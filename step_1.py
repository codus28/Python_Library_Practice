

# list comprehension

list_1 = [i for i in range(1,11) if i % 2 ==0]
print (list_1) # [2,4,6,8,10]


# dictionary comprehension

dict_1 = {i:i**2 for i in range(1,11) if i % 2 ==0}
print(dict_1) # {2:4, 4:16, 6:36, 8:64, 10:100}
