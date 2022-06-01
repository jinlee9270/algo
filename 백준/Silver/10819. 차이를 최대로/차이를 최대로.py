n = int(input())
nums = list(map(int, input().split()))
result = [0] * n
check = [False] * n
mx = 0


def recall(step):
    if step == n:
        s = 0
        for i in range(0, n-1):
          s = s + abs(result[i] - result[i - 1])

        global mx

        if mx < s:
            mx = s

    else:
        for i in range(0, n):
            if not check[i]:
                check[i] = True
                result[step] = nums[i]
                recall(step + 1)
                check[i] = False
                result[step] = 0


recall(0)
print(mx)
