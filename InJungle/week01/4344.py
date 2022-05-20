c = int(input())

for i in range(0, c):
    s = 0
    aver = 0
    count = 0
    student = list(map(int, input().split()))
    for j in range(1, len(student)):
        s = student[j] + s
        
    aver = s // student[0]

    for j in range(1, len(student)):
        if student[j] > aver:
            count = count + 1
    print("{:.3f}%".format(round(count / student[0] * 100, 3)))
