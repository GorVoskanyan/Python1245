import requests
import json
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice

def password_generator():
    password = ''
    n = ascii_lowercase + ascii_uppercase + digits + punctuation
    while len(password) < 8:
        password += choice(n)
    return password

url = 'https://api.github.com/users/hadley/orgs'
json_url = requests.get(url)
data = json.loads(json_url.text)
for i in data:
    i['password'] = password_generator()
with open('users.json', 'w') as file:
    json.dump(data, file, indent=2)