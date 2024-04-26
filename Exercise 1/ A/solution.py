# Python 3.12.1

def conditioner(room, cond, mode):
    if mode == 'freeze':
        print(min(cond, room))
    elif mode == 'heat':
        print(max(cond, room))
    elif mode == 'auto':
        print(cond)
    else:
        print(room)


troom, tcond = map(int, input().split())
cond_mode = input()
conditioner(troom, tcond, cond_mode)
