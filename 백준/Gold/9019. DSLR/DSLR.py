import sys
from collections import deque

t = int(input())


def bfs(start, end, visited):
    q = deque([('', start)])
    visited[start] = True

    while q:
        command, current = q.popleft()
        if current == end:
            return command

        num = (current * 2) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((command + 'D', num))

        num = (current - 1) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((command + 'S', num))

        num = (current % 1000) * 10 + current // 1000
        if not visited[num]:
            visited[num] = True
            q.append((command + 'L', num))

        num = (current % 10) * 1000 + current // 10
        if not visited[num]:
            visited[num] = True
            q.append((command + "R", num))


for _ in range(t):
    start, target = map(int, sys.stdin.readline().split())
    visited = [False] * 10000

    print(bfs(start, target, visited))
    