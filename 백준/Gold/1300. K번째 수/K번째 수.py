N = int(input())
K = int(input())
low = 1
high = K
number = 0

while low <= high:
    mid = (low + high) // 2
    temp = 0

    for i in range(1, N + 1):
        temp = temp + min(mid // i, N)

    if temp >= K:
        number = mid
        high = mid - 1
    else:
        low = mid + 1
print(number)
