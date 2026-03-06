T = int(input())

for t in range(1, T+1):
    A, B, K = map(int, input().split())
    S = A+B
    A_end = (A * pow(2, K, S)) % S
    ans = min(A_end, S-A_end)
    print(f'#{t} {ans}')