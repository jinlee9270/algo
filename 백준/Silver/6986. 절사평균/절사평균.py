import sys

n, k = map(int, input().split())
scores = []

for _ in range(n):
    scores.append(float(sys.stdin.readline().rstrip()))
scores.sort()

print('{:.2f}'.format(sum(scores[k:n-k]) / (n - (2 * k)) + 0.00000001))
print('{:.2f}'.format((sum(scores[k:n - k]) + (k * scores[k] + k * scores[n - k - 1])) / n + 0.00000001))
