import sys

def func(x, y, z):
    x = int(float(x))
    y = int(float(y))
    z = int(float(z))

    if x > y and z >= y:
        return ':)'
    elif y > x and y >= z:
        return ':('
    elif y > x and z > y and (z - y) < (y - x):
        return ':('
    elif y > x and z > y and (z - y) >= (y - x):
        return ':)'
    elif x > y and y > z and (y - z) < (x - y):
        return ':)'
    elif y > x and y > z and (y - z) >= (y - z):
        return ':('
    elif x == y and z > y:
        return ':)'
    else:
        return ':('


if not (__name__ == '__main__'): #PM | type_kill=random args=[221.4349579062564, 9947.921851960007, 1132.1665891368866]
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(func(x,y,z))