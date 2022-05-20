origin = list(input())
compare = list(input())
lcs = [[0] * ((len(compare)) + 1) for _ in range(((len(origin)) + 1))]

for i in range(1, len(origin) + 1):
    for j in range(1, len(compare) + 1):
        if origin[i - 1] == compare[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[-1][-1])
