n, c = map(int, input().split())

home = []
for i in range(0, n):
    home.append(int(input()))
home.sort()

left = 1
right = home[-1] - 1
dis = 0
MX_dis = 0
while left <= right:
    start_point = home[0]
    wifi = 1
    dis = (left + right) // 2

    for i in range(0, n):
        if home[i] - start_point >= dis:
            start_point = home[i]
            wifi = wifi + 1
            
    if wifi >= c:
        left = dis + 1
        if MX_dis < dis:
            MX_dis = dis
    else:
        right = dis - 1
print(MX_dis)
