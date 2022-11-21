import sys

def func1(a, b, c):
    if not (a > 10): #PM | type_kill=weakly args=[5514.57, 2157.07, 1759.0] | type_kill=strongly args=[5514.57, 2157.07, 1759.0] | type_kill=random args=[-6584.894352697302, -4687.454186876743, -6893.192442399186]
        for i in range(10):
            b += 1

    else:
        if b > 10:
            for i in range(5):
                c += 1

    return a, b, c

if __name__ == "__main__":
    a = float(sys.argv[1:][0])
    b = float(sys.argv[1:][1])
    c = float(sys.argv[1:][2])
    print(func1(a, b, c))
