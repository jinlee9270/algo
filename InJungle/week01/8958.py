n = int(input())

for i in range(0, n):
    quiz_result = input().split('X')
    count = 0
    for j in range(0, len(quiz_result)):
        temp = list(quiz_result[j])
        for k in range(len(temp), 0, -1):
            count = count + k
    print(count)
    
