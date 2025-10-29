import sys
sys.setrecursionlimit(10**6)
N, M, R = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [0] * (N+1)
for i in range(1, N + 1):
    graph[i].sort(reverse = True)

order = 1
def dfs(R):
    global order
    visited[R] = order
    for i in graph[R]:
        if visited[i] == 0:
            order += 1
            dfs(i)

dfs(R)
for i in range(1, N+1):
    print(visited[i])