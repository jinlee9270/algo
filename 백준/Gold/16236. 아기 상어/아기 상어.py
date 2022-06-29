import sys
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
r, c, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            r = i
            c = j
            break


def bfs(r, c, shark_size):
    distance = [[float("inf")] * n for _ in range(n)]
    q = deque([(r, c)])
    distance[r][c] = 0
    temp = []
    while len(q):
        cur = q.popleft()
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] > distance[cur[0]][cur[1]] + 1:
                if graph[nr][nc] <= shark_size:
                    q.append((nr, nc))
                    distance[nr][nc] = distance[cur[0]][cur[1]] + 1
                    if graph[nr][nc] < shark_size and graph[nr][nc] != 0:
                        temp.append((nr, nc, distance[nr][nc]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


fish = 0
answer = 0
while True:
    eat_fish = bfs(r, c, size)

    if len(eat_fish) == 0:
        break

    nr, nc, dist = eat_fish.pop()
    fish += 1
    answer += dist

    graph[r][c], graph[nr][nc] = 0, 0
    r, c = nr, nc

    if fish == size:
        size += 1
        fish = 0

print(answer)
