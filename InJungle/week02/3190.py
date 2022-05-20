from collections import deque

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    apple_x, apple_y = map(int, input().split())
    board[apple_x][apple_y] = 1


turn_points = {}
for _ in range(int(input())):
    item = input().split()
    if item[1] == "D":
        turn_points[int(item[0])] = 1
    else:
        turn_points[int(item[0])] = -1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

snake_direction = 0
board[1][1] = -1
snake_items = deque()
snake_items.append([1,1])

time = 0
while True:
    current_r, current_c = snake_items[0]

    if time in turn_points:
        snake_direction = (snake_direction + 4 + turn_points[time]) % 4

    next_r = current_r + dx[snake_direction]
    next_c = current_c + dy[snake_direction]

    if next_r < 1 or next_r > n or next_c < 1 or next_c > n:
        break

    if board[next_r][next_c] < 0:
        break

    if board[next_r][next_c] == 1:
        board[next_r][next_c] = 0 #사과 냠냠

    else:
        tail_r = snake_items[-1][0]
        tail_c = snake_items[-1][1]

        board[tail_r][tail_c] = 0 #뱀지나 간다
        snake_items.pop()

    board[next_r][next_c] = -1
    snake_items.appendleft([next_r, next_c])

    time = time + 1

print(time + 1)
