n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
pair_1 = 0
pair_2 = 0
mn = 2000000001
for index, candidate in enumerate(solutions):
    left = index + 1
    right = n - 1
    while left <= right:
        mid = (left + right) // 2

        if candidate + solutions[mid] == 0:
            pair_1 = candidate
            pair_2 = solutions[mid]
            break
        elif candidate + solutions[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1

        if mn > abs(candidate + solutions[mid]):
            mn = abs(candidate + solutions[mid])
            pair_1 = candidate
            pair_2 = solutions[mid]

print(pair_1, pair_2)
