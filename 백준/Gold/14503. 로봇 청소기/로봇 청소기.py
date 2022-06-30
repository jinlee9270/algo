n, m = map(int, input().split())
r, c, d = map(int, input().split())
graphs = []

for _ in range(n):
    graphs.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = True
cnt = 1

while True:
    flag = True
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and graphs[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            cnt += 1
            r = nr
            c = nc
            flag = False
            break
    if flag:
        if graphs[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dr[d], c - dc[d]
            