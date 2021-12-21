dwarf = []
total = 0
for i in range(0, 9):
    temp = int(input())
    dwarf.append(temp)
    total = total + temp

spy = total - 100
spy1 = 0
spy2 = 0
for i in range(0, 9):
    for j in range(0, 9):
        if i != j and dwarf[i] + dwarf[j] == spy:
            spy1 = dwarf[i]
            spy2 = dwarf[j]
            break

dwarf.sort()

for i in range(0, len(dwarf)):
    if dwarf[i] != spy1 and dwarf[i] != spy2:
        print(dwarf[i])
        
