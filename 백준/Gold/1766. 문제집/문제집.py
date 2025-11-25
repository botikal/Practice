import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,N+1)}
dependencies = [0] * (N+1)
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    dependencies[v2] +=1
end_points = []
for i in range(1, N+1):
    if dependencies[i] == 0:
        heapq.heappush(end_points, i)
ans_list = []
while end_points:
    now = heapq.heappop(end_points)
    ans_list.append(now)
    if dependencies[now] == 0:
        for j in graph[now]:
            dependencies[j] -= 1
            if dependencies[j] == 0:
                heapq.heappush(end_points, j)
print(*ans_list)