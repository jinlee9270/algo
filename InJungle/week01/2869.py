import math
a, b, v = map(int, input().split())
day = (v - a) % (a - b)

if day != 0:
    print((v - a) // (a - b) + 2)
else:
    print((v - a) // (a - b) + 1)
    
