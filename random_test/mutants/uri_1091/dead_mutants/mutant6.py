import sys

def func(dX,dY,x,y):
    dX = int(float(dX))
    dY = int(float(dY))

    x = int(float(x))
    y = int(float(y))

    if (x != dX or y == dY): #PM | type_kill=weakly args=[-8328.26, 6972.79, 9354.94, -8788.38] | type_kill=strongly args=[-8328.26, 6972.79, 9354.94, -8788.38] | type_kill=random args=[-8447.216395346204, 1727.5657105525079, -399.81794976759375, -7746.480019762985]
        return "divisa"
    elif x > dX and y > dY:
        return "NE"
    elif x > dX and y < dY:
        return "SE"
    elif x < dX and y > dY:
        return "NO"
    else:
        return "SO"


if __name__ == "__main__":
    dX = sys.argv[1:][0]
    dY = sys.argv[1:][1]
    x = sys.argv[1:][2]
    y = sys.argv[1:][3]
    print(func(dX,dY,x,y))