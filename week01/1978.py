prime_numbers = [True] * 1001
primes_N = []

for i in range(2, 1001):
    if prime_numbers:
        for j in range(i, 1000 // i + 1):
            prime_numbers[i * j] = False

for i in range(2, 1001):
    if prime_numbers[i]:
        primes_N.append(i)

n = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(0, n):
    if nums[i] in primes_N:
        count = count + 1
print(count)
