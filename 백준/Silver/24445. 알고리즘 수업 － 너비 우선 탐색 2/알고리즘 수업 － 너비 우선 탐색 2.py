from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for num in range(1, N+1):
    graph[num].sort(reverse=True)
visited = [0] * (N+1)
cue = deque([R])
order = 1
while cue:
    now = cue.popleft()
    if visited[now] == 0:
        visited[now] = order
        cue.extend(graph[now])
        order += 1
for j in range(1, N+1):
    print(visited[j])