import sys
mn = 9999999
n = int(input())
costs = [[0] * n for _ in range(n)]

result = [0] * n
check = [False] * n

for i in range(0, n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, n):
        costs[i][j] = temp[j]



def TSP(permu):
    global mn, n
    if n == permu:
        s = 0
        for i in range(0, n):
            now = result[i]
            to_go = result[(i + 1) % n]

            if costs[now][to_go] != 0:
                s = s + costs[now][to_go]
            else:
                return
        if mn > s:
            mn = s
    else:
        for i in range(0, n):
            if not check[i]:
                result[permu] = i
                check[i] = True
                TSP(permu + 1)
                check[i] = False
                result[permu] = 0

TSP(0)
print(mn)
