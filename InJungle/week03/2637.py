import sys
import collections

n = int(input())
m = int(input())
dp = [0] * (n + 1)
dp[n] = 1
edges = [[] for _ in range(n + 1)]
outdegree = [0] * (n + 1)

for _ in range(m):
    to_make, from_make, how_many = map(int, sys.stdin.readline().split())
    edges[to_make].append((from_make, how_many))
    outdegree[from_make] = outdegree[from_make] + 1
# print(edges)

deq = collections.deque()
for i in range(1, n + 1):
    if outdegree[i] == 0:
        deq.append(i)

while len(deq) > 0:
    vertex = deq.popleft()

    for nxt, value in edges[vertex]:
        dp[nxt] = dp[nxt] + dp[vertex] * value
        outdegree[nxt] = outdegree[nxt] - 1
        if outdegree[nxt] == 0:
            deq.append(nxt)

for i in range(1, n + 1):
    if len(edges[i]) == 0:
        print(i, dp[i])
        
