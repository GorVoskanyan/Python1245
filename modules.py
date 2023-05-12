# import requests
# import json
# from string import ascii_lowercase, ascii_uppercase, digits, punctuation
# from random import choice

# def password_generator():
#     password = ''
#     n = ascii_lowercase + ascii_uppercase + digits + punctuation
#     while len(password) < 8:
#         password += choice(n)
#     return password

# url = 'https://api.github.com/users/hadley/orgs'
# json_url = requests.get(url)
# data = json.loads(json_url.text)
# for i in data:
#     i['password'] = password_generator()
# with open('users.json', 'w') as file:
#     json.dump(data, file, indent=2)

# def login():
#     log = input('Enter Username: ')
#     pas = input('Enter Password: ')
#     for user in data:
#         if log == user['login'] and pas == user['password']:
#             print(f'Login: {user["login"]}\nId: {user["id"]}\nNode ID: {user["node_id"]}\nAvatar: {user["avatar_url"]}\n')
# login()

# def search(lst, x):
#     mid = len(lst) // 2
#     left_el = lst[((len(lst) // 2) -1)]
#     right_el = lst[((len(lst) // 2))]
#     if lst[mid] == x or left_el == x or right_el == x:
#         return x
#     elif mid == 0:
#         return 'Nshvac arjeqy bacakayum e listic'
#     elif x < left_el:
#         return search(lst[:mid], x)
#     elif x > right_el or mid == 1:
#         return search(lst[mid:], x)
#     return 'Nshvac arjeqy bacakayum e listic'


# print(search([1,2,3,5,6,8,9,10,11,13,14,16,19,20,22,33,55,66,88,99], 22))


# 1. FuncTiOn

def func(a,b,c):
    result = []
    if a > b:
        return 'Mutqagrvac e sxal arjeq'
    for i in range(a,b,c):
        result.append(i)
    return result

# 2. LisT

def lst_func(lst):
    new_lst =[]
    for i in range(0, len(lst) - 1):
        new_lst.append(lst[i] * lst[i+1])
    return new_lst

# 3. New senTence

def new_sentence(sentence, lst):
    new_text = ''
    index = -1
    for i in sentence:
        if i == '_':
            index += 1
            new_text += lst[index]
        else:
            new_text += i
    return new_text

# 4.sum wOrd

def sum_word(lst):
    s = sorted(lst, key=lambda n:  len(n))
    return len(s[0]) + len(s[-1])

# 5. find index ????????????????????????????????????????????????

def find_index(lst, num):
    if num in lst:
        return lst.index(num)
    else:
        pass
    
# print(find_index([ 36, -12, 47, -58, 148, -55, -19, 10], -56))

# 6.New DicT

def new_dct(num):
    dct = {}
    for i in range(1,num):
        dct[i] = i**2
    return dct

# 7.INVERT DicT

def invert_dct(dct):
    new_dct = {}
    for i in dct:
        if dct[i] not in new_dct:
            new_dct[dct[i]] = i
        else:
            lst = list(new_dct[dct[i]])
            new_dct[dct[i]] = lst + list(i)

    return new_dct

# 8. FIBONACCI

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)



# if __name__ == '__main__':
#     func()
#     lst_func()