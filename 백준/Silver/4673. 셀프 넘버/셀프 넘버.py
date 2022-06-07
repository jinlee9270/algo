One = 0
Ten = 0
Hund = 0
Thou = 0
Temp = 0
num = [0] * 10001
for i in range(1, 10001):
    Thou = i // 1000
    Temp = i % 1000
    Hund = Temp // 100
    Temp = i % 100
    Ten = Temp // 10
    One = Temp % 10
    if i+Thou+Hund+Ten+One <= 10000:
        num[i+Thou+Hund+Ten+One] = 1

# print(num)

for i in range(1, 10001):
    if num[i] == 0:
        print(i)
