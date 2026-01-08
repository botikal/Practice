import sys

V, E = map(int, sys.stdin.readline().split())
dist = [[1000000000] * (V+1) for i in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    dist[start][end] = cost
for k in range(1, V+1):
    for i in range(1, V+1):
        if dist[i][k] == 1000000000:
            continue
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
min_cycle = 1000000000

for i in range(1, V + 1):
    if dist[i][i] < min_cycle:
        min_cycle = dist[i][i]
if min_cycle == 1000000000:
    print(-1)
else:
    print(min_cycle)