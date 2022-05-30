n = int(input())

hidden_nums = list(input()) + ['#']

count = -1
nums = []
s = 0
for i in range(0, len(hidden_nums)):
    if 48 <= ord(hidden_nums[i]) <= 57:
        count = count + 1
        nums.append(int(hidden_nums[i]))
    else:
        index = 0
        while count >= 0:
            # print('nums=',nums, 'nums[index]=',nums[index], 's=',s, 'count=',count)
            s = s + (nums[index] * (10 ** count))
            count = count - 1
            index = index + 1
        nums.clear()

print(s)
