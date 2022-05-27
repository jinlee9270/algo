n = int(input())

times = list(map(int, input().split()))
times.sort()
answer = 0

for i in range(n + 1):
    answer += sum(times[:i])

print(answer)
