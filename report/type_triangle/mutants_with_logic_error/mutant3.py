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


if not (__name__ == '__main__'): #PM
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(type_triangle(x, y, z))