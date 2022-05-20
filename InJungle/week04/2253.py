n, m = map(int, input().split())
stones = [0] * (n + 1)
not_step = set()
dp = [[999999] * 143 for _ in range(n + 1)]
dp[1][0] = 0

for _ in range(m):
    not_step.add(int(input()))

for i in range(2, n + 1):
    if i in not_step:
        continue
    for j in range(1, 142):
        if i - j > 0:
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1


ans = min(dp[n])

if ans != 999999:
    print(ans)
else:
    print(-1)
    
