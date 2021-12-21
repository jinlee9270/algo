n = int(input())
result = [0] * n
check = [False] * n
mx = -999999
arr = list(map(int, input().split()))


def permu(step):
    global n, mx
    if step == n:
        s = 0
        for i in range(n - 1):
            s = s + abs(result[i] - result[i + 1])
        if mx < s:
            mx = s
    else:
        for i in range(n):
            if not check[i]:
                check[i] = True
                result[step] = arr[i]
                permu(step + 1)
                check[i] = False
                result[step] = 0


permu(0)
print(mx)
