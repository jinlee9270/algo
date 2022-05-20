def backtracking(rowPos):
    global answer

    if rowPos == n:
        answer = answer + 1
        return

    for col in range(n):
        flag = True
        for row in range(rowPos):
            if queenlocation[row] == col or rowPos - row == abs(col - queenlocation[row]):
                flag = False
                break
        if flag:
            queenlocation[rowPos] = col
            backtracking(rowPos + 1)


n = int(input())
answer = 0
queenlocation = [0] * n
backtracking(0)
print(answer)
