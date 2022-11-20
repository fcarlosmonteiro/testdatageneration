import sys

def func(x, y, z):
    x = int(float(x))
    y = int(float(y))
    z = int(float(z))

    if x > y and z >= y:
        return ':)'
    elif y > x and y >= z:
        return ':('
    elif (y > x and z < y and z - y < y - x): #PM | type_kill=weakly args=[-6546.85, -5409.61, -490.76]
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


if __name__ == "__main__":
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(func(x,y,z))