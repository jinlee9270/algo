import sys

n, m = map(int, input().split())

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

answer = list_a + list_b
answer.sort()

print(*answer)
