# Python 3.12.1

shop = dict()

with open('input.txt', 'rt', encoding='utf-8') as db:
    for line in db.readlines():
        name, goods, count = line.split()
        if name not in shop:
            shop[name] = dict()
        if goods not in shop[name]:
            shop[name][goods] = 0
        shop[name][goods] += int(count)

sort_name = sorted(shop)
for name in sort_name:
    sort_goods = sorted(shop[name])
    print(f'{name}:')
    for good in sort_goods:
        print(f'{good} {shop[name][good]}')
