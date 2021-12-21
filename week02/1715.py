import sys
import heapq
n = int(input())

nums = []
for i in range(0, n):
    heapq.heappush(nums, int(sys.stdin.readline()))

num_sum = 0
s = 0
for i in range(0, n - 1):
    temp = heapq.heappop(nums)
    num_sum = temp + heapq.heappop(nums)
    heapq.heappush(nums, num_sum)
    s = s + num_sum

print(s)
