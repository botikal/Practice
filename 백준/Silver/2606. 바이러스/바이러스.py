import sys

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = {i:[] for i in range(1, N + 1)}
for _ in range(V):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [0] * (N+1)
stack = [1]
while stack:
    now = stack.pop()
    if visited[now] == 0:
        visited[now] = 1
        stack.extend(graph[now])
print(sum(visited)-1)