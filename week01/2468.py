n = int(input())
maps = [[0] * n for _ in range(n)]

for i in range(0, n):
    a = list(map(int, input().split()))
    for j in range(0, n):
        maps[i][j] = a[j]


def bfs(x, y, rain):
    queue = [(x, y)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while len(queue) > 0:
        coor = queue.pop(0)
        for i in range(0, 4):
            nx = coor[0] + dx[i]
            ny = coor[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] > rain and visit[nx][ny]:
                visit[nx][ny] = False
                queue.append((nx, ny))


MX = 0
for i in range(0, 101):
    count = 0
    visit = [[True] * n for _ in range(n)]
    for j in range(0, n):
        for k in range(0, n):
            if i < maps[j][k] and visit[j][k]:
                visit[j][k] = False
                bfs(j, k, i)
                count = count + 1
    if MX < count:
        MX = count

print(MX)
