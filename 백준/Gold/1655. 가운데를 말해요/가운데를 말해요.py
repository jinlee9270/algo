import heapq
import sys

n = int(input())
min_heap = []
max_heap = []

for i in range(0, n):
    num = int(sys.stdin.readline())

    if len(max_heap) == 0 and len(min_heap) == 0:
        heapq.heappush(max_heap, -num)
    elif len(max_heap) - 1 == len(min_heap):
        pop_num = -heapq.heappop(max_heap)

        heapq.heappush(max_heap, -min(num, pop_num))
        heapq.heappush(min_heap, max(num, pop_num))
    elif len(min_heap) == len(max_heap):
        pop_num = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -min(num, pop_num))
        heapq.heappush(min_heap, max(num, pop_num))
    #
    # print('len(min_heap)',len(min_heap),'min_heap=','max_heap=',max_heap,len(max_heap))
    #
    # if len(min_heap) == len(max_heap):
    #     print(min(-max_heap[0], min_heap[0]))
    # elif len(max_heap) > len(min_heap):
    #     print(-max_heap[0])

    # print(max_heap, min_heap)
    # print('answer {}'.format(-max_heap[0]))
    # print()
    print(-max_heap[0])
