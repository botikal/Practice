N, M = map(int, input().split())
base_list = [i for i in range(1, N + 1)]

def backtrack(para_list, select):
    if select == M:
        print(*para_list)
        return
    for i in range(N):
        if base_list[i] not in para_list:
            para_list.append(base_list[i])
            backtrack(para_list, select + 1)
            para_list.pop()

backtrack([], 0)