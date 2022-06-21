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


def make_wall(r, c, cnt):
    if cnt > 3:
        return

    #  어느 시점에 벽 3개를 이미 다 세웠음. 더 볼 필요 없음
    if cnt == 3:
        bfs()
        return
    
    # 다 돌았음. cnt가 3 미만인 경우에도 더 돌 곳이 없으니 끝냄
    if r == n:
        return

    new_c = (c + 1) % m
    new_r = r + 1 if new_c == 0 else r

    make_wall(new_r, new_c, cnt)

    if maps[r][c] == 0:
        maps[r][c] = 1
        make_wall(new_r, new_c, cnt + 1)
        maps[r][c] = 0


n, m = map(int, input().split())
maps = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

answer = 0
make_wall(0, 0, 0)
print(answer)
