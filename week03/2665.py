import sys

def bfs(x,y):
    global n
    queue = [[x, y]]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while len(queue) > 0:
        # print(maze_info)
        coor = queue.pop(0)
        for i in range(4):
            nx = coor[0] + dx[i]
            ny = coor[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maze_info[nx][ny] > maze_info[coor[0]][coor[1]]:
                queue.append([nx, ny])
                if maze[nx][ny] == 1: #흰방일때
                    maze_info[nx][ny] = maze_info[coor[0]][coor[1]]
                else: #검은방일때
                    maze_info[nx][ny] = maze_info[coor[0]][coor[1]] + 1
    print(maze_info[n-1][n-1])


n = int(input())
maze = [[0] * n for _ in range(n)]
maze_info = [[99999999] * n for _ in range(n)]
maze_info[0][0] = 0
for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(n):
        maze[i][j] = int(temp[j])
# print(maze)

bfs(0,0)
# print(maze_info)
