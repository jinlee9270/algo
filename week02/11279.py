import heapq
import sys

n = int(input())
heap = []
heapq.heapify(heap)

for i in range(0, n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            max_heap = heapq.heappop(heap)
            print(abs(max_heap))
    else:
        heapq.heappush(heap, -num)
        
