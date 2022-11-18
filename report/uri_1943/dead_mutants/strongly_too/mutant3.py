import sys

def func(x):
    x = float(x)
    if x == 1:
        return "Top 1"
    elif x <= 3:
        return "Top 3"
    elif not (x <= 5): #PM | type_kill=weakly args=[4] | type_kill=strongly args=[4]
        return "Top 5"
    elif x <= 10:
        return "Top 10"
    elif x <= 25:
        return "Top 25"
    elif x <= 50:
        return "Top 50"
    else:
        return "Top 100"


if __name__ == "__main__":
    x = sys.argv[1:][0]
    print(func(x))