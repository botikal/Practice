import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph_up = {i:[] for i in range(1, N+1)}
indegree = [0] * (N+1)
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph_up[v1].append(v2)
    indegree[v2] += 1
end_points = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        end_points.append(i)
ans_list = []
while end_points:
    now = end_points.popleft()
    if indegree[now] == 0:
        ans_list.append(now)
        for j in graph_up[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                end_points.append(j)
print(*ans_list)