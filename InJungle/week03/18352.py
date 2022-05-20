import sys


def bfs(start):
    queue = [start]

    while len(queue) > 0:
        coor = queue.pop(0)

        for next_vertex in edges[coor]:
            if cost[next_vertex] > cost[coor] + 1:
                cost[next_vertex] = cost[coor] + 1
                queue.append(next_vertex)

    for index, ans in enumerate(cost):
        if ans == k:
            k_dis.append(index)
    k_dis.sort()


n, m, k, x = map(int, input().split())
edges = [[] for _ in range(n + 1)]
cost = [999999] * (n + 1)
cost[x] = 0
k_dis = []

for _ in range(m):
    x1, x2 = map(int, sys.stdin.readline().split())
    edges[x1].append(x2)
# print(edges)


bfs(x)
if len(k_dis) > 0:
    for v in k_dis:
        print(v)
else:
    print(-1)
    
