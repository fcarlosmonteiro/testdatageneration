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
    elif (x > dX and y > dY): #PM | type_kill=weakly args=[3217.15, 2297.51, 4854.34, -63.65] | type_kill=random args=[-1485.9592934532466, 1018.5855252605106, -9963.754610494952, 6433.034565208334]
        return "NO"
    else:
        return "SO"


if __name__ == "__main__":
    dX = sys.argv[1:][0]
    dY = sys.argv[1:][1]
    x = sys.argv[1:][2]
    y = sys.argv[1:][3]
    print(func(dX,dY,x,y))