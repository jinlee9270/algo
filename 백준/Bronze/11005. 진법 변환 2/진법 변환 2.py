N, b = input().split()
n = int(N)
B = int(b)

trans_B = []
while n > 0:
    trans_B.append(n % B)
    n = n // B

# print(trans_B)
for i in range(len(trans_B) - 1, -1, -1):
    if 10 <= trans_B[i] <= 35:
        print(chr(trans_B[i] + 55), end='')
    else:
        print(trans_B[i], end='')
