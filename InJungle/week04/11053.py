n = int(input())

seq = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = 1

for i in range(0, n):
    mx = 0
    for j in range(i - 1, -1, -1):
        if seq[i] > seq[j]:
            if mx < dp[j]:
                mx = dp[j]
        dp[i] = mx + 1

print(max(dp))
