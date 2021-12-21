prime_numbers = [True] * 10001
prime_numbers[0] = False
prime_numbers[1] = False
for i in range(2, 10001):
    if prime_numbers:
        for j in range(i, 10000 // i + 1):
            prime_numbers[i * j] = False

t = int(input())
for i in range(0, t):
    num = int(input())
    ans_j = 0
    ans_num = 0
    MN = 10000
    for j in range(2, num):
        if prime_numbers[num - j] and prime_numbers[j] and j <= num - j:
            if MN > (num - j) - j:
                MN = (num - j) - j
                ans_num = num - j
                ans_j = j
    print(ans_j, ans_num)
