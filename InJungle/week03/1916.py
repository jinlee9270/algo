import sys

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distances = [INF] * (n + 1)

for _ in range(m):
    x1, x2, x3 = map(int, input().split())
    graph[x1].append([x2, x3])

start, end = map(int, input().split())


def dijkstra(start):
    queue = [[0, start]]

    while len(queue) > 0:
        dist, now = queue.pop(0)

        if distances[now] < dist:
            continue

        for node in graph[now]:
            if distances[node[0]] > dist + node[1]:
                distances[node[0]] = dist + node[1]
                queue.append([dist + node[1], node[0]])


dijkstra(start)

print(distances[end])
