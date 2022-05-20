computer = int(input())
edge = int(input())
edges = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)


def bfs(start):
    queue = [start]
    visited[start] = True
    count = 0
    while len(queue) > 0:
        count = count + 1
        vertex = queue.pop()
        for next_vertex in edges[vertex]:
            if not visited[next_vertex]:
                queue.append(next_vertex)
                visited[next_vertex] = True
    print(count - 1)


for i in range(edge):
    u, v = map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)
# print(edges)

bfs(1)
