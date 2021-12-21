import sys

n = int(input())
maps = []
colors = [0, 0]
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))


def recall(x, y, search_area):
    start = maps[x][y]
    for i in range(x, x + search_area):
        for j in range(y, y + search_area):
            if start != maps[i][j]:
                recall(x, y, search_area//2)
                recall(x + search_area//2, y, search_area//2)
                recall(x, search_area//2 + y, search_area//2)
                recall(x + search_area//2, y + search_area//2, search_area//2)
                return

    if start == 0:
        colors[0] = colors[0] + 1
    else:
        colors[1] = colors[1] + 1


recall(0, 0, n)
print(colors[0])
print(colors[1])
