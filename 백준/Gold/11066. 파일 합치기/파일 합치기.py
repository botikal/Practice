import sys

T = int(sys.stdin.readline())
for t in range(T):
    K = int(sys.stdin.readline())
    K_nums = list(map(int, sys.stdin.readline().split()))
    base_list = [0] * (K+1)
    for i in range(K):
        base_list[i+1] = base_list[i] + K_nums[i]
    dp = [[0]*K for _ in range(K)]
    opt = [[0]*K for _ in range(K)]
    for i in range(K):
        opt[i][i] = i
    for size in range(2, K+1):
        for i in range(K-size+1):
            j = i + size - 1
            range_sum = base_list[j+1] - base_list[i]
            k_end = opt[i+1][j]
            k_start = opt[i][j-1]
            min_val = float('inf')
            best_k = -1
            for k in range(k_start, k_end+1):
                if k < K-1:
                    current_cost = dp[i][k] + dp[k+1][j] + range_sum
                    if current_cost < min_val:
                        min_val = current_cost
                        best_k = k
            dp[i][j] = min_val
            opt[i][j] = best_k
    print(dp[0][K-1])