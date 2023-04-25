# Упражнение 183. Последовательность химических
# элементов
name = input('Մուտքագրեք քիմիական տարր: ')
new_lst = []
def game(name):
    lst =  ['hydrogen','nitrogen','nickel','lanthanum','magnesium','beryllium','mendelevium']
    if name not in lst:
        return 'Այդպիսի քիմիական տարր գոյություն չունի\nԴՈՒՔ ՊԱՐՏՎԵՑԻՔ'
    elif name in lst:
        new_lst.append(name)
        name2 = input("Մուտքագրեք քիմիական տարր: ")
        if name[len(name) - 1] == name2[0] and name2 not in new_lst:
            name = name2
            return game(name)
        return 'ԴՈՒՔ ՊԱՐՏՎԵՑԻՔ'


print(game(name))