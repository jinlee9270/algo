import sys

n = int(input())
sticks = []
for _ in range(n):
    sticks.append(int(input()))

MX = 0
count = 0
for i in range(n-1, -1, -1):
    if MX < sticks[i]:
        MX = sticks[i]
        count = count + 1

print(count)
