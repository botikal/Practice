import sys

N, M = map(int, sys.stdin.readline().split())
dist = [float('inf')] * (N+1)
dist[1] = 0
routes = []
for i in range(M):
    start, finish, time = map(int, sys.stdin.readline().split())
    routes.append((start, finish, time))
negative_cycle = False
for j in range(N):
    for route in routes:
        start, finish, time = route
        if dist[start] != float('inf') and dist[start] + time < dist[finish]:
            if j == N-1:
                negative_cycle = True
            dist[finish] = dist[start] + time
if negative_cycle:
    print(-1)
else:
    for k in range(2, N + 1):
        if dist[k] == float('inf'):
            print(-1)
        else:
            print(dist[k])