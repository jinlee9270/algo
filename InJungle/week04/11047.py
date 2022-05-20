n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
for coin in coins:
    while k // coin > 0:
        count = count + k // coin
        k = k % coin
        # print(k)

print(count)
