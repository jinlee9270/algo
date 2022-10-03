import sys
from functools import cmp_to_key


def comparer(a,b):
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    return 0


test_case = int(input())

for i in range(0, test_case):
    n, m = sys.stdin.readline().split()
    book = int(n)
    student = int(m)
    student_wanted = []
    for j in range(0, student):
        s, e = sys.stdin.readline().split()
        student_wanted.append((int(s), int(e)))
    sorted_student_wanted = sorted(student_wanted, key=cmp_to_key(comparer))
    # print(sorted_student_wanted)
    book_list = [True] * (book + 1)
    count = 0
    for j in range(0, student):
        for k in range(sorted_student_wanted[j][0], sorted_student_wanted[j][1] + 1):
            if book_list[k]:
                book_list[k] = False
                count = count + 1
                break
            # print(k, book_list,sorted_student_wanted[j][0],sorted_student_wanted[j][1])
        # print(book_list)
    print(count)
    