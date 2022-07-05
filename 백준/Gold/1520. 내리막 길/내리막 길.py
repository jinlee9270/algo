import sys
import heapq

r, c = map(int, input().split())
origin = [[] for _ in range(r)]
dp = [[0] * c for _ in range(r)]
dp[0][0] = 1
heap = []

for i in range(r):
    temp = sys.stdin.readline().split()
    for j in range(c):
        origin[i].append(int(temp[j]))
        heapq.heappush(heap, (-int(temp[j]), j, i))

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

while len(heap) > 0:
    h_info = heapq.heappop(heap)
    height = -h_info[0]
    for i in range(4):
        nr = h_info[2] + dr[i]
        nc = h_info[1] + dc[i]
        if 0 <= nr < r and 0 <= nc < c and height < origin[nr][nc]:
            dp[h_info[2]][h_info[1]] = dp[h_info[2]][h_info[1]] + dp[nr][nc]

print(dp[r-1][c-1])
