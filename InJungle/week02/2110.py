n, c = map(int, input().split())

home = []
for i in range(0, n):
    home.append(int(input()))
home.sort()

left = 0
right = home[-1]
dis = 0
MX_dis = 0
while left <= right:
    start_point = home[0]
    wifi = 1
    dis = (left + right) // 2

    for i in range(0, n):
        # print(home[i],start_point,dis)
        if home[i] - start_point >= dis:
            start_point = home[i]
            wifi = wifi + 1
            # print("start_point",start_point,"dis=",dis,"wifi=",wifi)

    if wifi >= c:
        left = dis + 1
        # print(MX_dis,dis)
        if MX_dis < dis:
            MX_dis = dis
            # print(MX_dis)
    else:
        right = dis - 1
    # print(dis,wifi)
print(MX_dis)
