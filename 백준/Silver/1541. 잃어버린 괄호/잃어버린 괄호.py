line = list(input().split('-'))
curr_sum = 0
for ele in range(len(line)):
    if '+' in line[ele]:
        nums = list(map(int, line[ele].split('+')))
        sums = sum(nums)
        if ele == 0:
            curr_sum += sums
        else:
            curr_sum -= sums
    else:
        num = int(line[ele])
        if ele == 0:
            curr_sum += num
        else:
            curr_sum -= num
print(curr_sum)