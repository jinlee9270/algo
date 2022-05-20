n, m = map(int,input().split())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def bfs(start):
    queue = [start]
    visited[start] = True
    while len(queue) > 0:
        vertex = queue.pop()
        for next_vertex in edges[vertex]:
            if not visited[next_vertex]:
                queue.append(next_vertex)
                visited[next_vertex] = True


for i in range(m):
    u, v = map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)
# print(edges)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count = count + 1

print(count)
