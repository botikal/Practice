N, K = map(int, input().split())
coin_types = []
for _ in range(N):
    c_type = int(input())
    coin_types.append(c_type)
coins_used = 0
for i in range(N-1, -1, -1):
    while coin_types[i] <= K:
        coins = K // coin_types[i]
        K -= coins * coin_types[i]
        coins_used += coins
print(coins_used)