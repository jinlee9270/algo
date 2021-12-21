n, need_tree = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort(reverse=True)

left = 0
right = trees[0]
mid = 0
height = 0
while left <= right:
    mid = (left + right) // 2
    cutted_tree = 0

    for i in range(0, n):
        if trees[i] > mid:
            cutted_tree = cutted_tree + (trees[i] - mid)
        else:
            break

    if cutted_tree >= need_tree:
        left = mid + 1
        if height < mid:
            height = mid
    else:
        right = mid - 1

print(height)
