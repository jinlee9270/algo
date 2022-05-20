import sys

n = int(input())
strings = sys.stdin.readline().rstrip()
length = len(strings)
candidates = []
temp = strings

while True:
    left_string = ''
    right_string = ''

    for i in range(length):
        if i % 2 == 0:
            left_string = left_string + temp[i]
        else:
            right_string = right_string + temp[i]

    temp = left_string + right_string[::-1]
    candidates.append(temp)

    if temp == strings:
        break

print(candidates[(n % len(candidates)) - 1])
