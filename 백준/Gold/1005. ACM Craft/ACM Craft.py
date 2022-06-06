import sys
import collections

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    working_set = list(map(int, sys.stdin.readline().split()))
    inbound = [0] * (n + 1)
    rules = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)

    for _ in range(k):
        from_make, to_make = map(int, sys.stdin.readline().split())
        rules[from_make].append(to_make)
        inbound[to_make] = inbound[to_make] + 1
    w = int(input())

    deq = collections.deque()
    for i in range(1, n + 1):
        if inbound[i] == 0:
            deq.append(i)
            dp[i] = working_set[i - 1]

    while len(deq) > 0:
        now = deq.popleft()

        for nxt in rules[now]:
            inbound[nxt] = inbound[nxt] - 1
            dp[nxt] = max(dp[nxt], working_set[nxt - 1] + dp[now])

            if inbound[nxt] == 0:
                deq.append(nxt)
    # print(dp)
    print(dp[w])
    