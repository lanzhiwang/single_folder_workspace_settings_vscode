def add(a, b):
    x = a + 1
    y = b + 2
    return x + y

def main(i, j):
    i = i + 3
    j = j + 4
    return add(i, j)

if __name__ == "__main__":
    x = 2
    y = 3
    r = main(x, y)
    print(r)
