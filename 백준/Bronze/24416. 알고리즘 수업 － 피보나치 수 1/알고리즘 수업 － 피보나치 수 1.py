N = int(input())


def fib_recur(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fib_dp(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    attempt = 0
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        attempt += 1
    return attempt


print(fib_recur(N), fib_dp(N))