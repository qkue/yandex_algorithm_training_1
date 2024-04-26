# Python 3.12.1

symbols = set('0123456789qazwsxedcrfvtgbyhnujmikoplQAZWSXEDCRFVTGBYHNUJMIKOLP_')

with open('input.txt', 'rt', encoding='utf-8') as file:
    n, c, d = file.readline().rstrip().split()
    if c == 'no':
        key_set = {file.readline().rstrip().lower() for _ in range(int(n))}
    else:
        key_set = {file.readline().rstrip() for _ in range(int(n))}
    text = file.read()

#print(text.split())
ident = dict()

temp = []
for sym in text:
    if sym in symbols:
        temp.append(sym)
    else:
        if temp:
            if d == 'no' and temp[0].isdigit():
                temp.clear()
                continue

            identificator = ''.join(temp)
            
            if c == 'no':
                identificator = identificator.lower()
            if identificator in key_set:
                temp.clear()
                continue
            if identificator.isdigit():
                temp.clear()
                continue
            ident[identificator] = ident.get(identificator, 0) + 1
            temp.clear()

max_value = max(ident.values())
for k, v in ident.items():
    if v == max_value:
        print(k)
        break
