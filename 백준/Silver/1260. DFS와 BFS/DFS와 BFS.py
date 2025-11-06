import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for j in range(1, N+1):
    graph[j].sort()
visited_b = [0] * (N+1)
visited_d = [0] * (N+1)
queue = deque([V])
stack = [V]
ans_dfs = []
ans_bfs = []
while queue:
    now = queue.popleft()
    if visited_b[now] == 0:
        visited_b[now] = 1
        ans_bfs.append(now)
        queue.extend(graph[now])
while stack:
    now = stack.pop()
    if visited_d[now] == 0:
        visited_d[now] = 1
        ans_dfs.append(now)
        stack.extend(reversed(graph[now]))
print(*ans_dfs)
print(*ans_bfs)