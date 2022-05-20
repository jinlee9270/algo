import sys

data = []
head = 0
tail = len(data)
testcase = int(sys.stdin.readline())

for _ in range(testcase):
    com = list(map(str, sys.stdin.readline().split()))

    if com[0] == 'push':
        data.append(com[1])
        tail += 1
    elif com[0] == 'pop':
        if head == tail:
            print(-1)
        else:
            print(data[head])
            head += 1
    elif com[0] == 'size':
        print(tail - head)
    elif com[0] == 'empty':
        if tail - head == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if head == tail:
            print(-1)
        else:
            print(data[head])
    elif com[0] == 'back':
        if head == tail:
            print(-1)
        else:
            print(data[-1])
            
