import sys
from collections import deque

N = int(sys.stdin.readline())
mappy = []
for _ in range(N):
    line = list(sys.stdin.readline().strip())
    mappy.append(line)
group = 1
def bfs(start_y, start_x):
    cue = deque([(start_y, start_x)])
    mappy[start_y][start_x] = group
    while cue:
        now_y, now_x = cue.popleft()
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        for i in range(4):
            ny, nx = now_y + dy[i], now_x + dx[i]
            if 0<= ny < N and 0 <= nx < N:
                if mappy[ny][nx] == '1':
                    mappy[ny][nx] = group
                    cue.append((ny, nx))

for y in range(N):
    for x in range(N):
        if mappy[y][x] == '1':
            bfs(y, x)
            group += 1
per_group_count = []
for i in range(1, group):
    i_count = 0
    for ky in range(N):
        i_count += mappy[ky].count(i)
    per_group_count.append(i_count)
per_group_count.sort()
print(group-1)
for j in per_group_count:
    print(j)