# List
# num = int(input('Mutqagreq tuv: '))
# lst = []
# while num != 0:
#     lst.append(num)
#     num = int(input('Mutqagreq tuv: '))
# print(lst)

# lst1 = ['a','b','c','d']
# lst2 = [12,56,85,65]
# dct = {}
# for i in range(0, len(lst1)):
#     dct[lst1[i]] = lst2[i]
# print(dct)

# from random import randint

# dct = {'a':1,'b':2,'c':3,'d':4}
# lst = []
# for i in dct:
#     lst.append(i)
# del dct[lst[randint(0,len(lst)-1)]]
# print(dct)

# dct = {'c':3,'a':4,'b':1,'d':2}
# dct1 = dict(sorted(dct.items()))
# print(dct1)
# dct3 = dict(sorted(dct.items(), key = lambda item: item[1]))
# print(dct3)

# 1. FuncTiOn
# Given three numbers a, b (a ≤ b) and step. Create an list of 
# evenly spaced elements starting from a to b spaced by 
# step. you have 3 argument:
# Input Output
# 1 5 1 [1, 2, 3, 4, 5]
# 10 100 20 [10, 30, 50, 70, 90]

# x = int(input('a :'))
# y = int(input('b :'))
# z = int(input('a<=b :'))
# def lst(x, y, z ):
#     anun = []
#     for i in range(x, y, z):
#         anun.append(i)
#     print(anun)
        

# lst(x,y,z)   


# 2. LisT
# Write a function. Create the list which elements are 
# products between two neighbours.
# Input Output
# [3, 7, 12, 5, 20, 0] [21, 84, 60, 100, 0]
# [1, 1, 4, 32, 6] [1, 4, 128, 192 ]

# x = input('Texadrel tvery storaketnerov: ').split(',')
# def lst(x):
#     new_x = []
#     for i in range(0,len(x) - 1):
#         new_x.append(int(x[i]) * int(x[i+1]))
#     return new_x 

print(lst(x))