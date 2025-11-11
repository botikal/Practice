import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = {i: i for i in range(1, 101)}
for _ in range(N+M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1] = v2
cue = deque([(1,0)])
visited = {1}
while cue:
    loc, stage = cue.popleft()
    if loc >= 100:
        print(stage)
        break
    else:
        for i in range(1,7):
            if i + loc <= 100:
                new_loc = graph[loc + i]
                new_stage = stage + 1
                if new_loc not in visited:
                    cue.append((new_loc,new_stage))
                    visited.add(new_loc)