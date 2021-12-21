import sys

def bfs(x,y):
    queue = [(x, y)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ans = []
    while len(queue) > 0:
        coor = queue.pop(0)
        # print(queue)
        # print(cost_info)
        for i in range(4):
            nx = coor[0] + dx[i]
            ny = coor[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and cost_info[nx][ny] > cost_info[coor[0]][coor[1]] + 1:
                cost_info[nx][ny] = cost_info[coor[0]][coor[1]] + 1
                queue.append((nx, ny))
    print(cost_info[n-1][m-1])


n, m = map(int, input().split())
maze = []
cost_info = [[99999999] * m for _ in range(n)]
cost_info[0][0] = 1
# print("cost_info",cost_info)
# print(maze)
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))
# print("maze",maze)
bfs(0,0)
