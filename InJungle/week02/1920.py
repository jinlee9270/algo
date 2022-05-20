n = int(input())
nums = list(map(int, input().split()))
m = int(input())
my_ans = list(map(int, input().split()))

for i in range(0, m):
    if my_ans[i] in nums:
        print(1)
    else:
        print(0)
