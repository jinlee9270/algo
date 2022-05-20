queue = []
for i in range(int(input())):
    temp = int(input())
    if temp != 0:
        queue.append(temp)
    else:
        queue.pop()

print(sum(queue))
