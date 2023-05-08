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

def search(lst, x):
    mid = len(lst) // 2
    left_el = lst[((len(lst) // 2) -1)]
    right_el = lst[((len(lst) // 2))]
    if lst[mid] == x or left_el == x or right_el == x:
        return x
    elif mid == 0:
        return 'Nshvac arjeqy bacakayum e listic'
    elif x < left_el:
        return search(lst[:mid], x)
    elif x > right_el or mid == 1:
        return search(lst[mid:], x)
    return 'Nshvac arjeqy bacakayum e listic'


print(search([1,2,3,5,6,8,9,10,11,13,14,16,19,20,22,33,55,66,88,99], 19))
