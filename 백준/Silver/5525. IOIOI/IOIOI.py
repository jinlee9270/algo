import sys

N = int(input())
M = int(input())
S = sys.stdin.readline().rstrip()

answer, idx, count = 0, 0, 0

while idx < (M - 1):
    if S[idx : idx + 3] == 'IOI':
        idx = idx + 2
        count = count + 1
        if count == N:
            answer = answer + 1
            count = count - 1
    else:
        idx = idx + 1
        count = 0

print(answer)
