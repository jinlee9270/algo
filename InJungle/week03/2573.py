n, m = map(int, input().split())
maps = []


def ice(x, y):
    queue = [(x, y)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while len(queue) > 0:    
        coor = queue.pop(0)
        count = 0
        for i in range(4):
            nx = coor[0] + dx[i]
            ny = coor[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] and maps[nx][ny] != 0:
                queue.append((nx, ny))
                visit[nx][ny] = False
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                count = count + 1
        melt[coor[0]][coor[1]] = count
    # print(maps)
    # print(melt)
    for j in range(n):
        for k in range(m):
            if maps[j][k] - melt[j][k] < 0:
                maps[j][k] = 0
            else:
                maps[j][k] = maps[j][k] - melt[j][k]
    # print(maps)

    s = 0
    for j in range(n):
        for k in range(m):
            s = s + maps[j][k]

    if s == 0:
        return True


for i in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)

# print(maps)
year = 0
while True:
    ans = False
    area = 0

    melt = [[0] * m for _ in range(n)]
    visit = [[True] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # print(i, j)
            if maps[i][j] != 0 and visit[i][j]:
                visit[i][j] = False
                ans = ice(i, j)
                # print(ans)
                area = area + 1
                # print(area, year)

    if area > 1:
        print(year)
        break

    if ans:
        print(0)
        break

    year = year + 1
