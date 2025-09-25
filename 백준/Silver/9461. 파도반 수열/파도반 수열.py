T = int(input())
for t in range(1, T + 1):
    N = int(input())
    n_list = [0] * (N + 1)

    def padovan(n):
        if n >= 1:
            n_list[1] = 1
        if n >= 2:
            n_list[2] = 1
        if n >= 3:
            n_list[3] = 1
        if n >= 4:
            n_list[4] = 2
        if n >= 5:
            n_list[5] = 2
        for i in range(6, n + 1):
            n_list[i] = n_list[i-1] + n_list[i - 5]
        return n_list[n]
    ans = padovan(N)
    print(ans)