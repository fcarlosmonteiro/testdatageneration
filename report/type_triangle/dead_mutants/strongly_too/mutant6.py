import sys

def type_triangle(x, y, z):
    x = int(float(x))
    y = int(float(y))
    z = int(float(z))

    if x == y == z:
        return "Equilateral triangle"
    elif (x != y or y == z or z == x): #PM | type_kill=weakly args=[9406, 9405.27, -1155.19] | type_kill=strongly args=[9406, 9405.27, -1155.19]
        return "isosceles triangle"
    else:
        return "Scalene triangle"


if __name__ == "__main__":
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    z = sys.argv[1:][2]
    print(type_triangle(x, y, z))