n = int(input())

if 1 <= n <= 99:
    print(n)
elif 100 <= n <= 110:
    print(99)
else:
    if n == 1000:
        n = 999
    count = 0
    for i in range(111, n + 1):
        nums = []
        temp = i
        while temp > 0:
            nums.append(temp % 10)
            temp = temp // 10
        if nums[1] - nums[0] == nums[2] - nums[1]:
            count = count + 1
    print(count + 99)
    