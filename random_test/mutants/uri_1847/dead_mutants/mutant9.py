import sys

def func(x, y, z):
    x = int(float(x))
    y = int(float(y))
    z = int(float(z))

    if (x < y and z >= y): #PM | type_kill=weakly args=[5570.6, 2946.96, -9470.62] | type_kill=random args=[-8152.648342074662, 4191.195296772963, 9632.691095217524]
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


if __name__ == "__main__":
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(func(x,y,z))