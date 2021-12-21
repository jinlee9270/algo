import sys, heapq

n = int(sys.stdin.readline().rstrip())
degree = [0] * (n + 1)
result = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for num in range(1, n + 1):
    info = list(map(int, sys.stdin.readline().strip()))
    # print(info)
    for idx, value in enumerate(info):
        # print(idx, value)
        if value == 1:
            graph[idx + 1].append(num)
            degree[num] = degree[num] + 1

# print(graph)
# print(degree)

queue = []

for num in range(1, n + 1):

    if degree[num] == 0:
        heapq.heappush(queue, -num)
c = n
while queue:
    vertex = -heapq.heappop(queue)
    result[vertex] = c
    # print(result)
    for nxt in graph[vertex]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            heapq.heappush(queue, -nxt)
    c = c - 1


if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])
    
