import sys

def type_triangle(x, y, z):
    x = int(float(x))
    y = int(float(y))
    z = int(float(z))

    if x == y == z:
        return "Equilateral triangle"
    elif x==y or y==z or z==x:
        return "isosceles triangle"
    else:
        return "Scalene triangle"


if __name__ != '__main__': #PM | type_kill=random args=[-3770.3785081045926, -4040.640403401454, -6443.542448291182]
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(type_triangle(x, y, z))