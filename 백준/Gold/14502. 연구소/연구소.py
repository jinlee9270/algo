import copy
import sys


def bfs():
    queue = []
    copied_maps = copy.deepcopy(maps)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(m):
            if copied_maps[i][j] == 2:
                queue.append((i, j))

    while len(queue) > 0:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and copied_maps[nx][ny] == 0:
                copied_maps[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    zero_cnt = 0
    for i in range(n):
        zero_cnt += copied_maps[i].count(0)

    answer = max(answer, zero_cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(cnt + 1)
                maps[i][j] = 0


n, m = map(int, input().split())
maps = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

answer = 0
make_wall(0)
print(answer)
