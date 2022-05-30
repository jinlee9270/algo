import sys

n, m = map(int, sys.stdin.readline().split())
videos = list(map(int, sys.stdin.readline().split()))

vm = max(videos)
left = vm
right = sum(videos)
answer = 10**9

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    tmp = 0

    for i in range(n):
        if tmp + videos[i] <= mid:
            tmp += videos[i]
        else:
            cnt += 1
            tmp = videos[i]

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        if vm <= mid < answer:
            answer = mid

print(answer)
