import sys

n = int(input())
nums = [0] * 10001

for i in range(0, n):
    temp = int(sys.stdin.readline())
    nums[temp] = nums[temp] + 1

for i in range(1, len(nums)):
    for j in range(0, nums[i]):
        sys.stdout.write('{}\n'.format(i))
