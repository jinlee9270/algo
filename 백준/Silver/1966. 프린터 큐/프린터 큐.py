import sys

for _ in range(int(input())):
    doc_n, target_n = map(int, sys.stdin.readline().split())
    pri = list(map(int, sys.stdin.readline().split()))
    print_q = []

    for i in range(len(pri)):
        print_q.append((i, pri[i]))

    cnt = 0
    while len(print_q) > 0:
        mx = 0
        for i in range(len(print_q)):
            if print_q[i][1] > mx:
                mx = print_q[i][1]

        if print_q[0][1] < mx:
            print_q.append(print_q.pop(0))

        else:
            candidate = print_q.pop(0)
            cnt += 1
            if candidate[0] == target_n:
                print(cnt)
                break
                