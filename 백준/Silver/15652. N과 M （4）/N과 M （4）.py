N, M = map(int, input().split())

def back(step, selected):
    if step == M:
        print(*selected)
        return
    elif step == 0:
        for i in range(1, N + 1):
            back(step + 1, selected + [i])
    else:
        for i in range(1, N + 1):
            if i >= selected[-1]:
                back(step + 1, selected + [i])

back(0, [])