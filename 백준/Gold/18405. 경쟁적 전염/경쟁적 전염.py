import sys

n, k = map(int, input().split())
incubator = []


def infection(end):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(queue) > 0:
        virus_num, x, y, time = queue.pop(0)

        if time > end:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and incubator[nx][ny] == 0:
                incubator[nx][ny] = virus_num
                queue.append((incubator[nx][ny], nx, ny, time + 1))


for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    incubator.append(temp)

queue = []
for i in range(n):
    for j in range(n):
        if incubator[i][j] != 0:
            queue.append((incubator[i][j], i, j, 1))


queue.sort()
end_time, final_x, final_y = map(int, input().split())

infection(end_time)
# print(incubator)
print(incubator[final_x - 1][final_y - 1])
