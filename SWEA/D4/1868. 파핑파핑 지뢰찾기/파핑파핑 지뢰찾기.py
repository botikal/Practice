from collections import deque

T = int(input())

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def click(y, x):
    coords_to_check = deque([(y, x)])
    mat[y][x] = counts[y][x]
    while coords_to_check:
        curr_y, curr_x = coords_to_check.popleft()
        if counts[curr_y][curr_x] == 0:
            for i in range(8):
                ny = curr_y + dy[i]
                nx = curr_x + dx[i]
                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue
                if mat[ny][nx] == -1:
                    mat[ny][nx] = counts[ny][nx]
                    coords_to_check.append((ny, nx))

for t in range(1, T+1):
    N = int(input())
    mat = [['' for _ in range(N)] for _ in range(N)]
    counts = [[0] * N for _ in range(N)]
    ans = 0
    for _ in range(N):
        line = input()
        for i in range(N):
            if line[i] == '.':
                mat[_][i] = -1
            if line[i] == '*':
                mat[_][i] = -2
    for y in range(N):
        for x in range(N):
            if mat[y][x] == -1:
                mine_count = 0
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    if mat[ny][nx] == -2:
                        mine_count += 1
                counts[y][x] = mine_count
    for y in range(N):
        for x in range(N):
            if mat[y][x] == -1 and counts[y][x] == 0:
                ans += 1
                click(y,x)
    for y in range(N):
        for x in range(N):
            if mat[y][x] == -1:
                ans += 1
                mat[y][x] = counts[y][x]
    print(f'#{t} {ans}')