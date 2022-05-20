for _ in range(int(input())):
    is_vps = True
    stack = []
    ps = list(input())
    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                is_vps = False
        # print(stack)
    if len(stack) > 0 or not is_vps:
        print("NO")
    else:
        print("YES")
        
