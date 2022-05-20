import sys

for _ in range(int(input())):
    n = int(input())
    candidate = []
    
    for i in range(n):
        doc, itw = map(int, sys.stdin.readline().split())
        candidate.append((doc, itw))
    
    candidate.sort()
    mn = 999999
    recruit = 0
    
    for document, interview in candidate:
        if mn > interview:
            mn = interview
            recruit = recruit + 1
            
    print(recruit)
    
