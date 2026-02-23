from collections import deque

T = int(input())
for t in range(1, T+1):
    V, E, vert_a, vert_b = map(int, input().split())
    line_of_edges = list(map(int, input().split()))
    graph = {i:[] for i in range(1, V+1)}
    for i in range(E):
        parent = line_of_edges[2 * i]
        child = line_of_edges[2 * i + 1]
        graph[parent].append(child)
    def bfs(node):
        size = 1
        checks = 0
        if node == vert_a:
            checks += 1
        elif node == vert_b:
            checks += 1
        child_nodes = deque(graph[node])
        while child_nodes:
            check = child_nodes.popleft()
            if check == vert_a:
                checks += 1
            elif check == vert_b:
                checks += 1
            child_nodes.extend(graph[check])
            size += 1
        if checks == 2:
            return (size, node)
        else:
            return (float('inf'),node)
    ans_list = []
    for vertex in range(1, V+1):
        size, node = bfs(vertex)
        ans_list.append((size, node))
    ans_list.sort()
    print(f'#{t} {ans_list[0][1]} {ans_list[0][0]}')