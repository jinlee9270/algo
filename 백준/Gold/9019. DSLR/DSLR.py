import sys
from collections import deque

def D(num):
    res = num * 2
    if res > 9999:
        res %= 10000

    return res


def S(num):
    res = num
    if res == 0:

        return 9999
    res -= 1

    return res


def L(num):
    front = num % 1000
    back = num // 1000
    res = front * 10 + back

    return res


def R(num):
    front = num % 10
    back = num // 10
    res = front * 1000 + back

    return res


def oper(start, target):
    queue = deque()
    visited = set()
    queue.append((start, ''))
    visited.add(start)

    while len(queue) > 0:
        current, oper = queue.popleft()
        if current == target:
            print(oper)
            return

        temp = D(current)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, oper+"D"))

        temp = S(current)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, oper+"S"))

        temp = L(current)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, oper+"L"))

        temp = R(current)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, oper+"R"))


for _ in range(int(input())):
    start, tartet = map(int, sys.stdin.readline().split())
    oper(start, tartet)
    