rest, more_rest, highway_len = map(int, input().split())
rest_areas = [0] + list(map(int, input().split())) + [highway_len]
rest_areas.sort()

# print(rest_areas)

left = 1
right = highway_len - 1
mn = 99999
while left <= right:
    mid = (left + right) // 2
    # print(mid)
    count = 0

    for i in range(1, len(rest_areas)):
        if rest_areas[i] - rest_areas[i - 1] > mid and rest_areas[i] - rest_areas[i - 1] - 1 > 0:
            count = count + (rest_areas[i] - rest_areas[i - 1] - 1) // mid

    if count > more_rest:
        left = mid + 1

    else:
        right = mid - 1
        if mn > mid:
            mn = mid

print(mn)
