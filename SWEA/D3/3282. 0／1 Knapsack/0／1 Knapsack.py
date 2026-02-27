T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    dp = [[0] * (K+1) for i in range(N+1)]
    items = []
    for _ in range(N):
        volume, cost = map(int, input().split())
        items.append((volume, cost))
    for i in range(1, N+1):
        volume_i, cost_i = items[i-1]
        for j in range(1, K+1):
            if volume_i > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-volume_i] + cost_i)
    print(f'#{t} {dp[N][K]}')