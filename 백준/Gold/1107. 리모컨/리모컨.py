import sys
target_channel = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broken = set(map(int, sys.stdin.readline().split()))
# print(broken)

answer = abs(100 - target_channel)
for i in range(0, 999900):
    available = True
    pressed_num = 0

    if i != 100:
        num = i
        while True:
            if num % 10 in broken:
                available = False
                break
            num = num // 10
            pressed_num = pressed_num + 1

            if num == 0:
                break

        if available:
            answer = min(answer, pressed_num + abs(i - target_channel))
    # print(i, answer, pressed_num, target_channel)

print(answer)
