v, e = map(int, input().split())
ancestors = [0] * 10001
edges = []


def union_find(node):
    if ancestors[node] == node:
        return node

    ancestors[node] = union_find(ancestors[node])
    return ancestors[node]


for i in range(e):
    a, b, c = map(int, input().split())
    # print(a, b, c)
    edges.append((c, a, b))
    ancestors[a] = a
    ancestors[b] = b

edges.sort(key=lambda x: x[0])
# print(edges)

s = 0
for cost, to, go in edges:
    # print(cost, to, go)
    to_ac = union_find(to)
    go_ac = union_find(go)
    if to_ac != go_ac:
        s = s + cost
        ancestors[to_ac] = go_ac

print(s)
