N = int(input())
k = int(input())

left, right = 1, k
ans = 0

while left <= right:
    mid = (left + right)//2
    count = 0
    for i in range(1, N+1):
        count += min(N, mid//i)
    if count >= k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)