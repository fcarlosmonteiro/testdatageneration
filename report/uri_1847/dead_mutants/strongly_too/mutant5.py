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
    elif not ((x > y and y > z and y - z < x - y)): #PM | type_kill=weakly args=[1305.23, -316.6, 2604.42] | type_kill=strongly args=[5570.6, 2946.96, -9470.62]
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