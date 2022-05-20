def bfs(start):
    queue = [start]
    visited[start] = 1
    while len(queue) > 0:
        # print(visited)
        vertex = queue.pop(0)
        for next_vertex in edges[vertex]:
            if visited[next_vertex] == -1:
                visited[next_vertex] = 1 - visited[vertex]
                queue.append(next_vertex)
            else:
                if visited[next_vertex] == visited[vertex]:
                    return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    visited = [-1] * (v + 1)
    edges = [[] for _ in range(v + 1)]
    for i in range(e):
        x1, x2 = map(int, input().split())
        edges[x1].append(x2)
        edges[x2].append(x1)

    is_bip = True
    for i in range(1, v + 1):
        if visited[i] == -1:
            if not bfs(i):
                is_bip = False
                break

    if is_bip:
        print("YES")
    else:
        print("NO")
