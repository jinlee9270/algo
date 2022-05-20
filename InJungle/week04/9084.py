for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    max_value = int(input())
    make_max_value = [0] * (max_value + 1)
    make_max_value[0] = 1

    for coin in coins:
        for j in range(coin, max_value + 1):
            make_max_value[j] = make_max_value[j] + make_max_value[j - coin]

    print(make_max_value[max_value])
