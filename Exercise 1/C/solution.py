tel = ''.join(t for t in input() if t.isdigit())
if len(tel) == 7:
	tel = '7495' + tel
elif tel[0] == '8':
	tel = '7' + tel[1:]

for _ in range(3):
    number = ''.join(t for t in input() if t.isdigit())
    
    if len(number) == 7:
        number = '7495' + number
    elif number[0] == '8':
		    number = '7' + number[1:]
    
    print('YES' if number == tel else 'NO')
