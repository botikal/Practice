import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

min_length = float('inf')
left = 0
right = 0
sum_result = 0
while True:
    if sum_result >= S:
        min_length = min(right-left, min_length)
        sum_result -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum_result += nums[right]
        right += 1
if min_length == float('inf'):
    print(0)
else:
    print(min_length)