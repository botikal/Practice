N = int(input())
times = list(map(int, input().split()))
times.sort()
ans = 0
for i in times:
    ans += i * N
    N -= 1
print(ans)