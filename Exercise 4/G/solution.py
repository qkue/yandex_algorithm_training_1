# Python 3.12.1

def deposit(name, sum):
    if name not in bank:
        bank[name] = 0
    bank[name] += int(sum)

def withdraw(name, sum):
    if name not in bank:
        bank[name] = 0
    bank[name] -= int(sum)

def balance(name):
    print(bank.get(name, 'ERROR'))

def transfer(name_1, name_2, sum):
    if name_1 not in bank:
        bank[name_1] = 0
    if name_2 not in bank:
        bank[name_2] = 0
    bank[name_1] -= int(sum)
    bank[name_2] += int(sum)

def income(percent):
    for name in bank:
        if bank[name] > 0:
            bank[name] += int(bank[name] * (int(percent) / 100))

bank = dict()

with open('input.txt', 'rt', encoding='utf-8') as db:
    for line in db.readlines():
        operation, *other = line.split()
        if operation == 'DEPOSIT':
            deposit(*other)
        elif operation == 'WITHDRAW':
            withdraw(*other)
        elif operation == 'BALANCE':
            balance(*other)
        elif operation == 'TRANSFER':
            transfer(*other)
        elif operation == 'INCOME':
            income(*other)
