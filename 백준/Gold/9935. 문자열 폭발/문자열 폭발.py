strings = list(input())
bomb_string = list(input())

stack = []
for string in strings:
    is_bomb = False
    if len(stack) < len(bomb_string) - 1:
        stack.append(string)

    else:
        if string == bomb_string[-1]:
            stack.append(string)
            # print(stack[len(stack) - len(bomb_string):])
            if stack[len(stack) - len(bomb_string):] == bomb_string:
                temp = 0
                while temp < len(bomb_string):
                    stack.pop()
                    temp = temp + 1
        else:
            stack.append(string)


if len(stack) > 0:
    print("".join(stack))
else:
    print("FRULA")
