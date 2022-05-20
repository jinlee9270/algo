import collections

deq = collections.deque(range(int(input()),0,-1))

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    else:
        deq.pop()
        deq.appendleft(deq.pop())
