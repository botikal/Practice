import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ans_list = [nums[0]]
for i in range(1, N):
    if ans_list[-1] < nums[i]:
        ans_list.append(nums[i])
    else:
        left, right = 0, len(ans_list) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[i] > ans_list[mid]:
                left = mid + 1
            else:
                right = mid - 1
        ans_list[left] = nums[i]
print(len(ans_list))