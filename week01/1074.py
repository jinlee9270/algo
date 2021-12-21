n, r, c = map(int, input().split())
ans = 0

while n > 0:
    n = n - 1
    # print(ans)
    if r < 2 ** n and c < 2 ** n:
        # print(0)
        ans = ans + (2 ** n) * (2 ** n) * 0
    elif r < 2 ** n <= c:
        # print(1)
        ans = ans + (2 ** n) * (2 ** n) * 1
        c = c - (2 ** n)
    elif r >= 2 ** n > c:
        # print(2)
        ans = ans + (2 ** n) * (2 ** n) * 2
        r = r - (2 ** n)
    else:
        # print(3)
        ans = ans + (2 ** n) * (2 ** n) * 3
        c = c - (2 ** n)
        r = r - (2 ** n)
print(ans)
