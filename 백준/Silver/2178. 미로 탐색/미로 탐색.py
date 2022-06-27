n, m = map(int, input().split())
maze = []
costs = [[9999999] * m for _ in range(n)]
costs[0][0] = 1
# print(costs)


for _ in range(0, n):
    nums = list(map(int, input()))
    maze.append(nums)
# print(maze)


def maze_finder(x, y):
    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]
    queue = [[x, y]]

    while len(queue) > 0:
        coor = queue.pop(0)
        # print(coor, costs)
        for i in range(0, 4):
            a = coor[0] + dx[i]
            b = coor[1] + dy[i]
            # print(a, b, maze[a][b], costs)
            if 0 <= a < n and 0 <= b < m and maze[a][b] == 1:
                if costs[a][b] > costs[coor[0]][coor[1]] + 1:
                    costs[a][b] = costs[coor[0]][coor[1]] + 1
                    queue.append([a, b])
                    maze[a][b] = 0
    print(costs[n-1][m-1])


maze_finder(0, 0)
