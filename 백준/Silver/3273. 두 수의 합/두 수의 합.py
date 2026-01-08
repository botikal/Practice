import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
x = int(sys.stdin.readline())
count = 0
left = 0
right = n-1
while left < right:
    two_sum = nums[left] + nums[right]
    if two_sum > x:
        right -= 1
    elif two_sum < x:
        left += 1
    elif two_sum == x:
        count += 1
        left += 1
print(count)