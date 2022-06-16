import sys

def combi(idx, start):
    if idx == 6:
        print(*results)

    else:
        for i in range(start, n):
            if visit[i] == 0:
                results[idx] = numbers[i]
                visit[i] = 1

                combi(idx + 1, i + 1)
                visit[i] = 0

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers == [0]:
        break
    
    n = numbers[0]
    numbers.pop(0)
    results = [0] * 6
    visit = [0] * n
    tmp = []
    combi(0, 0)
    print()
    