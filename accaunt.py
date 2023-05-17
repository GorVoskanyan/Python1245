users = [{
    'user_id': 1,
    'last_name': 'Suren',
    'first_name':'Papikyan',
    'adress': 'Armenia, Yerevan, 127',
    'phone': '+374123456789',
    'balance': 5000,
    'password': '123456',
    'history': {}
    },
    {
    'user_id': 2,
    'last_name': 'Simon',
    'first_name':'Sargsyan',
    'adress': 'Armenia, Yerevan, 956',
    'phone': '+374777789789',
    'balance': 4000,
    'password': '12345678',
    'history': {}
    },
        {
    'user_id': 3,
    'last_name': 'Ani',
    'first_name':'Isahakyan',
    'adress': 'Armenia, Yerevan, Amiryan 125',
    'phone': '+374789899789',
    'balance': 1000,
    'password': '123456789',
    'history': {}
    }
    ]
class BankAccaunt:
    def __init__(self, userid, lastname, firstname, adress, phone, balance,history):
        self.userid = userid
        self.lastname = lastname
        self.firstname = firstname
        self.adress = adress
        self.phone = phone
        self.balance = balance
        self.history = history
    def info(self):
        print(f'UserID: {self.userid}\nLast Name: {self.lastname}\nFirst Name: {self.firstname}\nAdress: {self.adress}\nPhone: {self.phone}')
    def cash_input(self, price):
        self.balance += price
        self.history['cash input'] = price
    def cash_out(self, price):
        if price > self.balance:
            print('Insufficient funds...')
        else:
            self.balance -= price
            self.history['cash out'] = price
    def transfer(self, price, us_id):
        if price <= self.balance:
            for n in users:
                if n['user_id'] == us_id:
                    n['balance'] += price
                    # stugelu hamar
                    #print(n['balance'])
            # else:
            #     print('nman id chi gtnvel')
        else:
            print('Insufficient funds...')

def login():
    log = False
    login = int(input('ID: '))
    password = input('Password: ')
    for i in users:
        if i['user_id'] == login and i['password'] == password:
            log = True
            accaunt = BankAccaunt(users[users.index(i)]['user_id'],users[users.index(i)]['last_name'],users[users.index(i)]['first_name'],users[users.index(i)]['adress'],users[users.index(i)]['phone'], users[users.index(i)]['balance'],users[users.index(i)]['history'])
            while log:
                print('====Menu====')
                print('Info')
                print('Balance')
                print('Transfer')
                print('Cash out')
                print('Cash input')
                print('History')
                print('Exit')
                print('===========')
                command = input('Command: ')
                if command == 'info'.lower():
                    accaunt.info()
                elif command == 'cash out'.lower():
                    price = float(input('Amount: '))
                    accaunt.cash_out(price)
                elif command == 'transfer'.lower():
                    us_id = float(input('Recipient ID: '))
                    price = float(input('Amount: '))
                    accaunt.transfer(price,us_id)
                elif command == 'cash input'.lower():
                    price = float(input('Amount: '))
                    accaunt.cash_input(price)
                elif command == 'balance'.lower():
                    print('Your balance:', accaunt.balance)
                elif command == 'history'.lower():
                    print(accaunt.history)
                elif command == 'exit'.lower():
                    print('EXIT...')
                    break
                else:
                    print('Command error...')
                    break
login()