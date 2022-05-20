x_axis = [0]
y_axis = [0]

x, y = map(int, input().split())
n = int(input())
x_axis.append(x)
y_axis.append(y)

for i in range(0, n):
    axis, cut = map(int, input().split())
    if axis == 0:
        y_axis.append(cut)
    else:
        x_axis.append(cut)

x_axis.sort()
y_axis.sort()
new_x_axis = []
new_y_axis = []
for i in range(1, len(x_axis)):
    new_x_axis.append(x_axis[i] - x_axis[i - 1])
for i in range(1, len(y_axis)):
    new_y_axis.append(y_axis[i] - y_axis[i - 1])

MX = 0
for i in range(len(new_x_axis)):
    for j in range(len(new_y_axis)):
        if MX < new_x_axis[i] * new_y_axis[j]:
            MX = new_x_axis[i] * new_y_axis[j]
print(MX)
