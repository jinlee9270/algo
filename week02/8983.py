def hunting(start, end):
    candidate = 2000000001
    left = 0
    right = len(hunting_zone) - 1
    while left <= right:
        mid = (left + right) // 2
        if start > hunting_zone[mid]:
            left = mid + 1

        else:
            right = mid - 1
            if candidate > hunting_zone[mid]:
                candidate = hunting_zone[mid]

    return candidate <= end


n, m , l = map(int, input().split())

hunting_zone = list(map(int,input().split()))
hunting_zone.sort()
death = 0
for i in range(m):
    animal_x, animal_y = map(int, input().split())

    if animal_y <= l:
        start_x = animal_x - (l - animal_y)
        end_x = animal_x + (l - animal_y)

        if hunting(start_x, end_x):
            death = death + 1

print(death)
