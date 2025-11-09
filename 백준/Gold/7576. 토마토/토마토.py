import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
case = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    case.append(line)
start_coords = []
minus_counts = 0
for y in range(N):
    for x in range(M):
        if case[y][x] == 1:
            start_coords.append((y, x))
        elif case[y][x] == -1:
            minus_counts += 1
visited = [[0] * M for _ in range(N)]
cue = deque()
for ty, tx in start_coords:
    cue.append((ty, tx, 0))
    visited[ty][tx] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
time = 0

while cue:
    now_y, now_x, time = cue.popleft()
    for i in range(4):
        ny, nx = now_y + dy[i], now_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if visited[ny][nx] == 0 and case[ny][nx] == 0:
                visited[ny][nx] = 1
                case[ny][nx] = 1
                cue.append((ny, nx, time + 1))

gone_to = sum(sum(row) for row in visited)
if gone_to == (M * N) - minus_counts:
    print(time)
else:
    print(-1)