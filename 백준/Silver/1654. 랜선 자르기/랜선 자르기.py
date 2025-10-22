K, N = map(int, input().split())
list_of_nums = [int(input()) for _ in range(K)]
start, end = 1, max(list_of_nums)
ans = 0
while start <= end:
    med = (start + end) // 2
    pieces = 0
    for i in list_of_nums:
        pieces += i // med
    if pieces < N:
        end = med - 1
    else:
        ans = med
        start = med + 1
print(ans)