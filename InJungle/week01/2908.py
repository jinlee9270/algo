a, b = map(int, input().split())
list_a = []
list_b = []

while a > 0:
    list_a.append(a % 10)
    list_b.append(b % 10)
    a = a // 10
    b = b // 10

a_reverse = list_a[0] * 100 + list_a[1] * 10 + list_a[2]
b_reverse = list_b[0] * 100 + list_b[1] * 10 + list_b[2]

print(max(a_reverse, b_reverse))
