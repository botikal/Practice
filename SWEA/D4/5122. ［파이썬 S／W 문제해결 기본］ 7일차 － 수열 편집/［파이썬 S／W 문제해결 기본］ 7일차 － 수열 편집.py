T = int(input())

class Node:
    def __init__(self, v, next = None):
        self.v = v
        self.next = next

def insert(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    curr_node = head
    for _ in range(index - 1):
        if curr_node is None:
            break
        curr_node = curr_node.next
    new_node.next = curr_node.next
    curr_node.next = new_node
    return head

def delete(head, index):
    if index == 0:
        return head.next
    curr = head
    for _ in range(index - 1):
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return head

def change(head, index, value):
    curr_node = head
    for _ in range(index):
        if curr_node is None: break
        curr_node = curr_node.next
    if curr_node:
        curr_node.v = value


for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    head = None
    curr = None
    for i in range(N):
        if i == 0:
            head = Node(nums[i])
            curr = head
        else:
            curr.next = Node(nums[i])
            curr = curr.next
    for _ in range(M):
        command = input().split()
        type = command[0]
        if type == 'I':
            idx, val = int(command[1]), int(command[2])
            head = insert(head, idx, val)
            N += 1
        if type == 'D':
            idx = int(command[1])
            head = delete(head, idx)
            N -= 1
        if type == 'C':
            idx, val = int(command[1]), int(command[2])
            change(head, idx, val)
    if N <= L:
        print(f'#{t} -1')
    else:
        curr = head
        for _ in range(L):
            curr = curr.next
        print(f'#{t} {curr.v}')