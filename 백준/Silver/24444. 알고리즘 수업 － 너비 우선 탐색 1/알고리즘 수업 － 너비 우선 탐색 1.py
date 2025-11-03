from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for key in graph:
    graph[key].sort()
visited = [0] * (N + 1)
order = 1
def bfs(start):
    global order
    queue = deque([start])
    visited[start] = order
    while queue:
        v = queue.popleft()
        for nxt in graph[v]:
            if visited[nxt] == 0:
                order += 1
                visited[nxt] = order
                queue.append(nxt)
bfs(R)
for i in range(1, N + 1):
    print(visited[i])