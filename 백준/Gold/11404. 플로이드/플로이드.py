import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dist = [[float('inf')] *(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i][i] = 0
for i in range(M):
    start, finish, cost = map(int, sys.stdin.readline().split())
    if dist[start][finish] > cost:
        dist[start][finish] = cost
for k in range(1, N+1):
    for i in range(1, N+1):
        if dist[i][k] == float('inf'):
            continue
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
for i in range(1, N+1):
    row = []
    for j in range(1, N+1):
        if dist[i][j]== float('inf'):
            row.append(0)
        else:
            row.append(dist[i][j])
    print(*row)