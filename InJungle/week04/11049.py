n = int(input())
matrix = []

for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[1000000] * n for _ in range(n)]

for i in range(0, n):
    dp[i][i] = 0

for i in range(1, n):
    for j in range(0, n - i):
        # print(i, n - i, j)
        row = j
        col = j + i
        dp[row][col] = dp[row][0] + dp[row + 1][col] + (matrix[row][0] * matrix[col][1] * matrix[row + 1][0])

        for k in range(i):
            dp[row][col] = min(dp[row][col],
                                   dp[row][k + col - i] + dp[1 + k + row][col] + matrix[row][0] * matrix[col][1] *
                                   matrix[row + k + 1][0])
print(dp[0][-1])
