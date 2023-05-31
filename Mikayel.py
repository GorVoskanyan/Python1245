# COVID 19
# from math import pi
# class Covid19:
#     def __init__(self, celsius):
#         self.celsius = celsius
    
#     def covid_test(self):
#         test = self.celsius * pi
#         if 120 <= round(test, 1) <= 128:
#             print('You Have coronavirus')
#         else:
#             print('Everything is ok')

# name = Covid19(float(input('Enter Celsius: ')))
# name.covid_test()

# Find your name number
# from math import sqrt
# class Name:
#     def __init__(self, name):
#         self.name = name
    
#     def name_num(self):
#         result = 0
#         for i in self.name:
#             if i == 'a' or i == 'j' or i == 's':
#                 result += 1
#             elif i == 'b' or i == 'k' or i == 't':
#                 result += 2
#             elif i == 'c' or i == 'l' or i == 'u':
#                 result += 3
#             elif i == 'd' or i == 'm' or i == 'v':
#                 result += 4
#             elif i == 'e' or i == 'n' or i == 'w':
#                 result += 5
#             elif i == 'f' or i == 'o' or i == 'x':
#                 result += 6
#             elif i == 'g' or i == 'p' or i == 'y':
#                 result += 7
#             elif i == 'h' or i == 'q' or i =='z':
#                 result += 8
#             elif i == 'i' or i == 'r':
#                 result += 9
#         if sqrt(result) < 5:
#             print(result, 'Yes')
#         else:
#             print(result, 'No')

# obj = Name(input('Enter name: ').lower())
# obj.name_num()

# Harry Potter
from random import choice
class HarryPotter:
    def __init__(self, name, points, words):
        self.name = name
        self.points = points
        self.words = words
inp = input('Enter magic word: ').lower()
lord = HarryPotter('Lord', 0, choice(['Avada Kedavra', 'Crucio', 'Imperio']).lower())
harry = HarryPotter('Harry', 0, inp)

while True:
    if lord.words == harry.words:
        harry.points += 1
        lord.points -= 1
    elif lord.words != harry.words:
        harry.points -= 1
        lord.points += 1
    print(lord.words)
    print(lord.name, lord.points, ' | ', harry.name, harry.points)
    if harry.points == 2:
        print('You win!')
        break
    elif lord.points == 2:
        print('You lose!')
        break
    inp = input('Enter magic word: ').lower()