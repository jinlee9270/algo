n, k = map(int, input().split())
weight = []
value = []
bags = [-1] * (k + 1)
bags[0] = 0

for i in range(0, n):
    w, v = input().split()
    weight.append(int(w))
    value.append(int(v))

for i in range(0, len(weight)):
    for j in range(k - weight[i], -1, -1):
        if bags[j] != -1 and bags[j + weight[i]] < bags[j] + value[i]:
            bags[j + weight[i]] = bags[j] + value[i]

print(max(bags))
