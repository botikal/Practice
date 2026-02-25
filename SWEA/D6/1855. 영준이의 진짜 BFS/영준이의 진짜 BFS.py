from collections import deque

Log = 20

def lca(node_a, node_b):
    if depth[node_a] < depth[node_b]:
        node_a, node_b = node_b, node_a
    diff = depth[node_a] - depth[node_b]
    for j in range(Log):
        if (diff >> j) & 1:
            node_a = up[node_a][j]
    if node_a == node_b:
        return node_a
    for j in range(Log-1, -1, -1):
        if up[node_a][j] != up[node_b][j]:
            node_a = up[node_a][j]
            node_b = up[node_b][j]
    return up[node_a][0]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    graph = {i:[] for i in range(1, N+1)}
    up = [[0] * Log for _ in range(N + 1)]
    depth = [0] * (N+1)
    parents = list(map(int, input().split()))
    for i in range(N-1):
        u = parents[i]
        v = i + 2
        graph[u].append(v)
        up[v][0] = u
    # now for calculating the depth and traverse order
    start = deque([(1, 0)])
    traverse_order = []
    while start:
        node, curr_depth = start.popleft()
        traverse_order.append(node)
        depth[node] = curr_depth
        for j in range(1, Log):
            up[node][j] = up[up[node][j - 1]][j - 1]
        for child in graph[node]:
            start.append((child, curr_depth+1))
    ans = 0
    for j in range(len(traverse_order)-1):
        node_u = traverse_order[j]
        node_v = traverse_order[j + 1]
        pivot = lca(node_u, node_v)
        ans += abs(depth[node_u] - depth[pivot]) + abs(depth[node_v] - depth[pivot])
    print(f'#{t} {ans}')