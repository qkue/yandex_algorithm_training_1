# Python 3.12.1

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


no_roots = 0
kx_roots = 1
one_xy_root = 2
one_x = 3
one_y = 4
inf_roots = 5

det = a * d - b * c
det_x = (e * d - b * f)
det_y = (a * f - e * c)
x_null = a == 0 and c == 0
y_null = b == 0 and d == 0

if det != 0:
    x = det_x / det
    y = det_y / det
    print(one_xy_root, x, y)

else:
    if (det_x == 0 and det_y == 0):
        if (x_null and y_null):
            if (e != 0 or f != 0):
                print(no_roots)
            
            else:
                print(inf_roots)
            
        
        elif x_null:
            if (b != 0):
                y = e / b
            
            else:
                y = f / d
                

            print(one_y, y)
        elif y_null:
            if a != 0:
                x = e / a
            
            else: 
                x = f / c

            print(one_x, x)
        else:
            
            if b != 0:
                bi = e / b
                k = -a / b
            else:
                bi = f / d
                k = -c / d

            print(kx_roots, k, bi)
        
        
    else:
        print(no_roots)
