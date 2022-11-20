import sys

def func(dX,dY,x,y):
    dX = int(float(dX))
    dY = int(float(dY))

    x = int(float(x))
    y = int(float(y))

    if x == dX or y == dY:
        return "divisa"
    elif x > dX and y > dY:
        return "NE"
    elif x > dX and y < dY:
        return "SE"
    elif not ((x < dX and y > dY)): #PM | type_kill=weakly args=[3217.15, 2297.51, 4854.34, -63.65] | type_kill=strongly args=[8897.94, -9103.35, -8211.03, -9519.08]
        return "NO"
    else:
        return "SO"


if __name__ == "__main__":
    dX = sys.argv[1:][0]
    dY = sys.argv[1:][1]
    x = sys.argv[1:][2]
    y = sys.argv[1:][3]
    print(func(dX,dY,x,y))