import sys

n = int(sys.stdin.readline())
road_map = {}
for i in range(n):
    i1, i2 = map(int, sys.stdin.readline().split())

    if i1 not in road_map:
        road_map[i1] = [i]
    else:
        road_map[i1].append(i)

    if i2 not in road_map:
        road_map[i2] = [i]
    else:
        road_map[i2].append(i)

points = sorted(list(road_map.items()))
l = int(sys.stdin.readline())


max_count = 0
include_count = 0
include_checker = [0] * n

start_index = 0
end_index = 0

for point_index, (x, items) in enumerate(points):
    if x <= points[start_index][0] + l:
        end_index = point_index

        for index in items:
            include_checker[index] = include_checker[index] + 1

            if include_checker[index] == 2:
                include_count = include_count + 1

max_count = include_count

for point_index, (start_point, items) in list(enumerate(points))[1:]:
    old_items = points[point_index - 1][1]

    for old_item in old_items:
        include_checker[old_item] = include_checker[old_item] - 1

        if include_checker[old_item] == 1:
            include_count = include_count - 1

    for end_index_candidate in range(end_index + 1, len(points)):
        if points[end_index_candidate][0] > start_point + l:
            break
        else:
            end_index = end_index_candidate

            for index in points[end_index_candidate][1]:
                include_checker[index] = include_checker[index] + 1

                if include_checker[index] == 2:
                    include_count = include_count + 1

    max_count = max(max_count, include_count)

print(max_count)
