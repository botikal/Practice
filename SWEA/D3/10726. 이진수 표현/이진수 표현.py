T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    comparison = (1 << N) -1
    if comparison == (M & comparison):
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')