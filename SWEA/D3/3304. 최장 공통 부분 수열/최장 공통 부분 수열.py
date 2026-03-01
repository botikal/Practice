T = int(input())
for t in range(1, T+1):
    word_a, word_b = map(list, input().split())
    len_a, len_b = len(word_a), len(word_b)
    dp = [[0] * (len_b+1) for _ in range(len_a+1)]
    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if word_a[i-1] == word_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f'#{t} {dp[len_a][len_b]}')