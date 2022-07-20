from collections import deque


def bfs(start, node):
    deq = deque()
    deq.append(start)
    visited = [False] * (node + 1)
    visited[start] = True
    cnt = 1

    while deq:
        cur = deq.popleft()
        for nxt in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                deq.append(nxt)
                cnt += 1

    return cnt


node, vertex = map(int, input().split())
edges = [[] for _ in range(node + 1)]

for _ in range(vertex):
    com1, com2 = map(int, input().split())
    edges[com2].append(com1)

results = []
mx = 0
for i in range(1, node + 1):
    candidate = bfs(i, node)
    results.append((i, candidate))
    if mx < candidate:
        mx = candidate

for i in range(node):
    if results[i][1] == mx:
        print(results[i][0], end=" ")
