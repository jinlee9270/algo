import sys

sys.setrecursionlimit(2 * 10 ** 5)

n = int(sys.stdin.readline())
s = 0
places = ['-']
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def recall(vertex):
    child_indoors = []

    for nxt in edges[vertex]:
        if not visited[nxt]:
            visited[nxt] = True
            child_indoors.append(recall(nxt))

    global s

    total_indoors = sum(child_indoors)

    if places[vertex]:
        s = s + total_indoors * 2
        return 1

    for indoor in child_indoors:
        s = s + indoor * (total_indoors - indoor)

    return total_indoors


for character in sys.stdin.readline().rstrip():
    if character == '1':
        places.append(1)
    else:
        places.append(0)

for _ in range(n - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    edges[v1].append(v2)
    edges[v2].append(v1)

visited[1] = True
recall(1)

print(s)
