n, r, c = map(int, input().split())
ans = 0

while n > 0:
    n = n - 1
    
    if r < 2 ** n and c < 2 ** n:
        ans = ans + (2 ** n) * (2 ** n) * 0
        
    elif r < 2 ** n <= c:
        ans = ans + (2 ** n) * (2 ** n) * 1
        c = c - (2 ** n)
        
    elif r >= 2 ** n > c:
        ans = ans + (2 ** n) * (2 ** n) * 2
        r = r - (2 ** n)
        
    else:
        ans = ans + (2 ** n) * (2 ** n) * 3
        c = c - (2 ** n)
        r = r - (2 ** n)
        
print(ans)
