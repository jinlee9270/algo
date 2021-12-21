import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def water():
    while len(water_queue) > 0:
        (cr, cc) = water_queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < r \
                    and 0 <= nc < c \
                    and water_map[nr][nc] > water_map[cr][cc] + 1:
                water_map[nr][nc] = water_map[cr][cc] + 1
                water_queue.append((nr, nc))


def dochi():
    while len(dochi_queue) > 0:
        (cr, cc) = dochi_queue.pop(0)

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < r \
                    and 0 <= nc < c \
                    and dochi_map[nr][nc] > dochi_map[cr][cc] + 1\
                    and water_map[nr][nc] > dochi_map[cr][cc] + 1:

                dochi_map[nr][nc] = dochi_map[cr][cc] + 1
                dochi_queue.append((nr, nc))


r, c = map(int, input().split())
origin_map = []
dochi_map = [[999999] * c for _ in range(r)]
water_map = [[999999] * c for _ in range(r)]

for _ in range(r):
    temp = list(sys.stdin.readline().rstrip())
    origin_map.append(temp)

water_queue = []
dochi_queue = []
beaver_r = 0
beaver_c = 0

for i in range(0, r):
    for j in range(0, c):
        if origin_map[i][j] == "D":
            water_map[i][j] = -1
            beaver_r = i
            beaver_c = j
        if origin_map[i][j] == "*":
            water_map[i][j] = 0
            water_queue.append((i, j))
        if origin_map[i][j] == "X":
            water_map[i][j] = -1
            dochi_map[i][j] = -1
        if origin_map[i][j] == "S":
            dochi_map[i][j] = 0
            dochi_queue.append((i, j))

water()

water_map[beaver_r][beaver_c] = 999999

dochi()


if dochi_map[beaver_r][beaver_c] != 999999:
    print(dochi_map[beaver_r][beaver_c])
else:
    print("KAKTUS")
    
