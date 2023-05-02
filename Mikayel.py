# Даны два списка. Создайте словарь, ключами которого являются элементы
# первого списка, а значениями – элементы второго, находящиеся в
# соответствующих позициях.

# names = ['Armen', 'Artur','Ani', 'Vazgen']
# ages = [15,26,5,53]
# print(dict(zip(names, ages)))

# Дан словарь. Напишите программу, которая удаляет случайный элемент
# словаря.

# from random import randrange
# dct = {'a':1, 'b':2, 'c':3,'d': 4, 'e':5,'f':6}
# x = randrange(0, len(dct))
# key = list(dct.keys())
# dct.pop(key[x])
# print(dct)

# Дан словарь, ключами которого являются строки, а значениями – числа.
# Выведите его на экран сначала в отсортированном по ключам виде (plustilino)в
# алфавитном порядке), затем – отсортированным по возрастанию значений.

# dct = {'c':2, 'b':1, 'a':5,'d': 4, 'e':3,'f':6}
# dct_sort_keys = dict(sorted(dct.items(), key=lambda i: i[0]))
# dct_sort_values = dict(sorted(dct.items(), key=lambda i: i[1]))
# print(dct_sort_keys)
# print(dct_sort_values)

# Дан словарь, в котором ключами являются названия товаров, а значениями
# – их цены. Напишите программу, которая выводит на экран товары и цены,
# запрашивает у пользователя, что он хочет купить, в каком количестве, и
# считает общую цену покупки.

# apranq = {'notbook': 800, 'phone': 450, 'watch': 150}
# for i in apranq.items():
#     print(f'{i[0]} - {i[1]}$')
# price = 0
# name = input('Enter name: ')
# while name != '':
#     quality = int(input('Quality: '))
#     for i in apranq:
#         if name == i:
#             price += apranq[i] * quality
#     print(f'Ընդամենը։ {price} $')
#     name = input('Enter name: ')
# print(f'Total price: {price}$')

# Напишите программу, которая читает текстовый файл и помещает его
# содержимое в список строк.

# with open('names.txt', 'r') as file:
#     lst = file.readlines()
#     print(lst)

# Напишите программу, которая считает сколько раз в файле встречается
# заданное слово.

# bar = input('Bar: ')
# with open('text.txt', 'r') as file:
#     txt = file.read()
#     print(txt.count(bar))

# Определить, сколько в текстовом файле строк, слов и символов.
# from string import punctuation
# with open('text.txt', 'r') as file:
#     txt = file.read()
#     count = 0
#     for i in txt:
#         if i in punctuation:
#             count += 1
#     print(txt.count('\n') + 1)
#     print(txt.count(' ') + txt.count('\n') + 1)
#     print(count)

# Дан текстовый файл, каждая строка которого содержит название товара,
# его цену и количество. Напишите программу, которая помещает
# содержимое этого файла в словарь так, что каждая запись словаря
# соответствует одной строке файла. Ключом записи является название
# товара, значением – список, первый элемент которого цена, второй –
# количество товара.

# dct = {}
# with open('apranq.txt', 'r') as file:
#     for i in file.readlines():
#         dct[i.split(' ')[0]] = [int(i.split(' ')[1]), int(i.split(' ')[2])]
# print(dct)

# Имеется словарь, ключами которого являются товары, а значениями – их
# цена. Запишите данные словаря в файл так, чтобы в каждой строке
# находилась одна запись словаря.

# dct = {'notbook': 800, 'phone': 450, 'watch': 150}
# with open('price.txt', 'w', encoding='utf-8') as file:
#     for i in dct.items():
#         file.write(str(i[0]) + ' ' + str(i[1]) + '\n')

# В текстовом файле заменить все символы табуляции четырьмя пробелами.
# ??????????? chi ashxatum?????????????
with open('tab.txt', 'r') as file:
    text = file.read()
with open('tab.txt', 'w', encoding='utf-8') as update_file:
    text_list = text.split('\t')
    print(text_list)
    update_file.write('    '.join(text_list))
