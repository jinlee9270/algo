num_oper = input().split("-")

nums = []
for i in range(len(num_oper)):
    nums.append(num_oper[i].split("+"))
# print(nums)

first = 0
minus = 0
for i in range(0, len(nums)):
    for j in range(len(nums[i])):
        if i == 0:
            first = first + int(nums[i][j])
        else:
            minus = minus + int(nums[i][j])

print(first - minus)
