dp = [0, 1, 2]
n = int(input())

for i in range(3, n + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % 15746)

print(dp[n])
