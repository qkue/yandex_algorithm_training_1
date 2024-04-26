# Python 3.12.1
# В задаче нужно рассмотреть различные случаи, она не стоит времени потраченного на неё и если пропустите ничего не потеряете.

def trivial_cases(flat, storeys, flat_train, entrance_train, floor_train):
    if storeys < floor_train:
        #этажность меньше исследуемого(кв2) этажа
        return -1, -1
    
    if flat_train < (storeys * (entrance_train-1) + floor_train):
        # кв2 меньше минимально возможного значения на `floor_train`(на каждом этаже минимум одна квартира)
        return -1, -1
    
    if entrance_train == 1 and floor_train == 1:
        # кв2 расположена в 1-ом подъезде и на 1-ом этаже.
        
        if flat <= flat_train:
            # исследуемая квартира расположена до кв2.
            return 1, 1
            
        if flat <= storeys: # flat > 1, storeys > 1
            # квартира расположена в 1-ом подъезде(на каждом этаже минимум одна квартира)
            return 1, 0
        
        if storeys == 1:
            #этажность=1
            return 0, 1
        
        # больше ничего не сможем определить(если кв2 в 1 подъезде, на 1 этаже).
        return 0, 0
        
    # в противном случае возвращаем `False` и продолжаем поиск нетривиальных случаев.
    return False

def get_entrance_and_floor(flats_per_floor):
    entrance = flat // (storeys*flats_per_floor) + int(
                                                        flat % (storeys*flats_per_floor) != 0 )

    floor = (flat -storeys*flats_per_floor*(entrance-1)) // flats_per_floor + int(
                                                                                   (flat - storeys*flats_per_floor*(entrance-1)) % flats_per_floor != 0 )
    return entrance, floor

def main_deсision(flat, storeys, flat_train, entrance_train, floor_train):
    flats_per_floor_min = flat_train // ( storeys * (entrance_train - 1) + floor_train ) + int(
                                                    flat_train % ( storeys * (entrance_train - 1) + floor_train ) != 0)
    flats_per_floor_max = (flat_train - 1) // ( storeys * (entrance_train - 1) + floor_train - 1)

    if (flats_per_floor_min > flats_per_floor_max) or (flats_per_floor_min < 1) or (flats_per_floor_max > 1000000):
    # не знаю почему, но на всякий - добавил flats_per_floor_max > 1000000 
        return -1, -1

    entrance_main, floor_main = get_entrance_and_floor(flats_per_floor_min)

    for flats in range(flats_per_floor_min+1, flats_per_floor_max+1):
        entrance, floor = get_entrance_and_floor(flats)

        if entrance != entrance_main:
            entrance_main = 0
        if floor != floor_main:
            floor_main = 0
        if entrance_main == 0 and floor_main == 0:
            break
            
    if flat <= storeys and entrance_main != 1:
        # если `flat' в 1-ом подъезде и `entrance_main` рассчиталось неверно
        entrance_main = 1
    
    return entrance_main, floor_main
            


flat, storeys, flat_train, entrance_train, floor_train = map(int, input().split())

trivial_deсision = trivial_cases(flat, storeys, flat_train, entrance_train, floor_train)
if trivial_deсision:
    print( *trivial_deсision)
else:
    print( *main_deсision(flat, storeys, flat_train, entrance_train, floor_train) )
