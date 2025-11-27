import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = {i:[] for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))
dist = [float('inf')] * (V+1)
pq = []
dist[K] = 0
heapq.heappush(pq,(0, K))
while pq:
    curr_cost, now = heapq.heappop(pq)
    if dist[now] < curr_cost:
        continue
    for weight, next in graph[now]:
        cost = weight + curr_cost
        if cost < dist[next]:
            dist[next] = cost
            heapq.heappush(pq, (cost, next))
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])