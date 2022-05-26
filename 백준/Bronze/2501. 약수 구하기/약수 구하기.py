n, k = map(int, input().split())
cds = []

for i in range(1, n + 1):
    if n % i == 0:
        cds.append(i)

if len(cds) < k:
    print(0)
else:
    print(cds[k - 1])
