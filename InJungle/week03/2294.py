n, k = map(int, input().split())
values = [999999] * (k + 1)
values[0] = 0
coins = []

for _ in range(n):
    coins.append(int(input()))

for i in range(n):
    for j in range(k - coins[i] + 1):
        if values[j + coins[i]] > values[j] + 1:
            values[j + coins[i]] = values[j] + 1

if values[k] != 999999:
    print(values[k])
else:
    print(-1)
    
