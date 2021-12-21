n, m, v = map(int, input().split())
edges = [[] * (n + 1) for _ in range(n + 1)]


def dfs(vertex, checks):
    print(vertex,end=" ")

    for next_vertex in edges[vertex]:
        # print(' {} > {} {}'.format(vertex, next_vertex, next_vertex not in checks))
        if next_vertex not in checks:
            checks.add(next_vertex)
            dfs(next_vertex, checks)

    # print('end of search {}'.format(vertex))


def bfs(vertex):
    queue = [vertex]

    checks = set()
    checks.add(vertex)

    while len(queue) > 0:
        # print('less queue: {}'.format(queue))

        vertex = queue.pop(0)

        print(vertex,end=" ")

        for next_vertex in edges[vertex]:
            # print(' {} > {} {}'.format(vertex, next_vertex, next_vertex not in checks))
            if next_vertex not in checks:
                checks.add(next_vertex)
                queue.append(next_vertex)


for _ in range(m):
    v1, v2 = map(int, input().split())

    edges[v1].append(v2)
    edges[v2].append(v1)

for i in range(n + 1):
    edges[i].sort()

s = set()
s.add(v)
dfs(v, s)

print()

bfs(v)
