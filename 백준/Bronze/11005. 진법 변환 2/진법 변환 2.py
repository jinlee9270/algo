n, b = map(int, input().split())
new_nums = []

while n > 0:
    new_nums.append(n % b)
    n = n // b

for i in range(len(new_nums) -1, -1, -1):
    if 10 <= new_nums[i]:
        print(chr(55 + new_nums[i]), end='')
    else:
        print(new_nums[i], end='')
