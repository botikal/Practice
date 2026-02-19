class Node:
    def __init__(self):
        self.data = None
        self.left_val = None
        self.right_val = None
for t in range(1, 11):
    N = int(input())
    nodes = [Node() for _ in range(N+1)]
    ans_string = []
    def in_order_traversal(node):
        if node is None:
            return
        in_order_traversal(node.left_val)
        ans_string.append(node.data)
        in_order_traversal(node.right_val)
    for i in range(N):
        line = list(input().split())
        curr_id = int(line[0])
        curr_val = line[1]
        nodes[curr_id].data = curr_val
        line_len = len(line)
        if line_len > 2:
            left_id = int(line[2])
            nodes[curr_id].left_val = nodes[left_id]
            if line_len > 3:
                right_id = int(line[3])
                nodes[curr_id].right_val = nodes[right_id]
    root = nodes[1]
    in_order_traversal(root)
    print(f'#{t} {"".join(ans_string)}')