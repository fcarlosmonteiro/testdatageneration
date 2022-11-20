import sys
import math

def func(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    

    if a == 0:
        return "Impossivel calcular"
    else:
        d = b**2 - 4*a*c

        if d < 0:
            return "Impossivel calcular"
        else:
            r1 = (-b-math.sqrt(d))/(2*a)
            r2 = (-b+math.sqrt(d))/(2*a)


            return "R1 = {:.5f}\nR2 = {:.5f}".format(r2, r1)

if __name__ == "__main__":
    a = sys.argv[1:][0]
    b = sys.argv[1:][1]
    c = sys.argv[1:][2]
    print(func(a, b, c))