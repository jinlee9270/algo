n, m = map(int, input().split())
heavy = [[] for _ in range(n + 1)]
light = [[] for _ in range(n + 1)]


def dfs(vertex, edges, checks):
    for nxt in edges[vertex]:
        if nxt not in checks:
            checks.add(nxt)
            dfs(nxt, edges, checks)

    return not len(checks) > n // 2


for _ in range(m):
    v1, v2 = map(int, input().split())
    heavy[v1].append(v2)
    light[v2].append(v1)

count = 0
for i in range(1, n + 1):
    heavy_set = set()
    light_set = set()

    dfs(i, light, light_set)
    dfs(i, heavy, heavy_set)

    if len(light_set) > n // 2 or len(heavy_set) > n // 2:
        count = count + 1

print(count)
