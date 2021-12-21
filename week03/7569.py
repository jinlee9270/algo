import sys
from collections import deque
m, n, h = map(int, input().split())
tomato_boxes = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
# print(tomato_boxes)


def bfs():

    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]
    dz = [1, -1, 0, 0, 0, 0]

    while len(queue) > 0:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomato_boxes[nz][nx][ny] == 0:
                    tomato_boxes[nz][nx][ny] = tomato_boxes[z][x][y] + 1
                    queue.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            # print(i, j, k)
            tomato_boxes[i][j][k] = temp[k]

# print(tomato_boxes)
queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_boxes[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
is_fresh = True
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_boxes[i][j][k] == 0:
                is_fresh = False
                break
            result = max(result, tomato_boxes[i][j][k])

if not is_fresh:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
    
