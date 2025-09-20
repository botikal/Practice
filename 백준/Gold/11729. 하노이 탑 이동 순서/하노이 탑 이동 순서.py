N = int(input())
size = [0] * (N + 1)
size[1] = 1
for n in range(2, N + 1):
    size[n] = 1 + 2 * size[n-1]

pillars = [1, 2, 3]
def hanoi(height, start, dest):
    if height == 1:
        return [[start, dest]]
    excl_ele = pillars.copy()
    excl_ele.remove(start)
    excl_ele.remove(dest)
    return hanoi(height -1, start, *excl_ele) + [[start, dest]] + hanoi(height-1, *excl_ele, dest)

ans_list = hanoi(N, 1, 3)

print(size[N])
for i in range(size[N]):
    print(*ans_list[i])