N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = mat[0]

for i in range(1, N):
    dp[i][0] = mat[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = mat[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = mat[i][2] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[N-1]))