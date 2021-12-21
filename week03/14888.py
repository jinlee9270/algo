n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # 0(+), 1(-), 2(*), 3(//)

MX = -1000000001
MN = 1000000001
count = 0


def recall(count, total, plus, minus, multiply, divide):
    global MX, MN, n

    if count == n:
        MX = max(total, MX)
        MN = min(total, MN)
        return

    else:
        if plus > 0:
            recall(count + 1, total + nums[count], plus - 1, minus, multiply, divide)
        if minus > 0:
            recall(count + 1, total - nums[count], plus, minus - 1, multiply, divide)
        if multiply > 0:
            recall(count + 1, total * nums[count], plus, minus, multiply - 1, divide)
        if divide > 0:
            recall(count + 1, int(total / nums[count]), plus, minus, multiply, divide - 1)


recall(1, nums[0], operators[0], operators[1], operators[2], operators[3])

print(MX)
print(MN)
