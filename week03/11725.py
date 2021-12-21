import sys

sys.setrecursionlimit(100000)

n = int(input())

tree = [[] for _ in range(n + 1)]
partents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(start, tree, parents):
    # print(partents,start)
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, tree, partents)

for i in range(2, n + 1):
    print(partents[i])
