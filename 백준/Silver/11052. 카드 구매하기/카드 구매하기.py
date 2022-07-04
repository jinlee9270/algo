import sys
n = int(input())
num = input().split()

money_for_card = [0]
for i in range(0, len(num)):
    money_for_card.append(int(num[i]))

for i in range(0, n + 1):
    for j in range(1, i):
        if money_for_card[i] < money_for_card[i - j] + money_for_card[j]:
            money_for_card[i] = money_for_card[i - j] + money_for_card[j]
            
print(money_for_card[n])
