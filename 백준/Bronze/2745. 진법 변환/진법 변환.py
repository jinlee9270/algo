n, b = input().split()
B = int(b)
N = list(n)
N.reverse()

s = 0
for i in range(0, len(N)):
    if ord('A') <= ord(N[i]) <= ord('Z'):
        s = s + ((ord(N[i]) - 55) * (B ** i))
    else:
        s = s + (int(N[i]) * (B ** i))
    # print(s)

print(s)
