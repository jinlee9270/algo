import sys

n, m = input().split()
N = int(n)
M = int(m)

nums = []
for i in range(0, N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
# print(nums)
MN_minus = 2000000001
s = 1

for i in range(0, len(nums) - 1):
    for j in range(s, len(nums)):
        v = nums[j] - nums[i]

        if v < M:
            continue
        else:
            MN_minus = min(MN_minus, v)
            s = j
            break

print(MN_minus)
