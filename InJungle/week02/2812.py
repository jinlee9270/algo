n, k = map(int, input().split())
nums = list(map(int, input()))

stack = []
pop_count = 0

for num in nums:
    while len(stack) > 0 and stack[-1] < num and pop_count < k:
        stack.pop()
        pop_count = pop_count + 1

    stack.append(num)

while pop_count < k:
    stack.pop()
    pop_count = pop_count + 1

for num in stack:
    print(num, end="")
    
