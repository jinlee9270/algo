def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


start = int(input())

ans = factorial(start)
print(ans)
