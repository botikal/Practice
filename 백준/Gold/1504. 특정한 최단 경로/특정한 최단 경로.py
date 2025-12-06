import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, N+1)}
for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph[v1].append((w, v2))
    graph[v2].append((w, v1))
r1, r2 = map(int, sys.stdin.readline().split())
def dijk(start):
    duration = [float('inf')] * (N+1)
    pq = []
    duration[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        curr_dur, now = heapq.heappop(pq)
        if duration[now] < curr_dur:
            continue
        for time, next in graph[now]:
            cost = time + curr_dur
            if cost < duration[next]:
                duration[next] = cost
                heapq.heappush(pq, (cost, next))
    return duration
start_locs = [1, r1, r2]
distances = []
for loc in start_locs:
    distances.append(dijk(loc))
ans = min(distances[0][r1] + distances[1][r2] + distances[2][N],
          distances[0][r2] + distances[2][r1] + distances[1][N])
print(ans if ans < float('inf') else -1)