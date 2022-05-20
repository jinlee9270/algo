def move(num, x, y):

    if num >= 1:
        move(num - 1, x, 6 - x - y)
        print(x, y)
        move(num - 1, 6 - x - y, y)


n = int(input())

if n <= 20:
    print(2 ** n - 1)
    move(n, 1, 3)
else:
    print(2 ** n - 1)
