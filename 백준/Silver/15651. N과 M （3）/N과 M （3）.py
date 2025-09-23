N, M = map(int, input().split())


def back(inc, par_list):
    if inc == M:
        print(*par_list)
        return
    for i in range(1, N + 1):
        back(inc + 1, par_list + [i])


back(0, [])