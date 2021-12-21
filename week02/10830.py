import sys


def squ_here(m1, m2):
    global n
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] = (m3[i][j] + m1[i][k] * m2[k][j]) % 1000
    return m3


def recall(A, B):
    if B == 1:
        return A
    x = recall(A, B//2)
    if B % 2 != 0:
        return squ_here(squ_here(x, x), A)
    else:
        return squ_here(x, x)


n, squ = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# new_matrix = [[0] * n for _ in range(n)]
if squ != 1:
    print("\n".join(map(lambda x: " ".join(map(str, x)), recall(matrix, squ))))
else:
    new_matrix = recall(matrix, squ)
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[i][j] % 1000
    print("\n".join(map(lambda x: " ".join(map(str, x)), new_matrix)))
