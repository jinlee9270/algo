from collections import deque
N, K = map(int, input().split())
answer = []

queue = deque([x + 1 for x in range(N)])

while len(queue):
    for _ in range(K):
        queue.append((queue.popleft()))
    answer.append(str(queue.pop()))

print('<%s>' % ', '.join(answer))
