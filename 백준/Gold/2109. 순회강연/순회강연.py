import sys
import heapq
n = int(input())

schedules = []
for i in range(0, n):
    a, b = sys.stdin.readline().split()
    schedules.append((int(b), int(a)))
schedules.sort()

heap = []
for i in range(0, n):
    if len(heap) < schedules[i][0]:
        heapq.heappush(heap, schedules[i][1])
    else:
        if heap[0] < schedules[i][1]:
            heapq.heappushpop(heap, schedules[i][1])
        else:
            pass
    # print(heap)
print(sum(heap))
