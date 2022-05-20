import collections

v, e = map(int, input().split())
in_degree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    in_degree[v2] = in_degree[v2] + 1

deq = collections.deque()

for i in range(1, v + 1):
    if in_degree[i] == 0:
        deq.append(i)

while len(deq) > 0:
    node = deq.popleft()
    print(node, end=' ')

    for i in graph[node]:
        in_degree[i] = in_degree[i] - 1
        if in_degree[i] == 0:
            deq.append(i)
