class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, s, value):
        if s == 1:
            new_node = Node(value)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                current = self.tail
                current.next = new_node
                self.tail = new_node
        else:
            for i in range(s):
                new_node = Node(value[i])
                if self.head == None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    current = self.tail
                    current.next = new_node
                    self.tail = new_node

    def insert(self, x, y, s):
        if x == 0:
            old_head = self.head
            self.head = Node(s[0])
            current = self.head
            for i in range(1, y):
                new_node = Node(s[i])
                current.next = new_node
                current = new_node
            current.next = old_head
            return
        current = self.head
        for _ in range(x-1):
            current = current.next
        future_node = current.next
        for i in range(y):
            new_node = Node(s[i])
            current.next = new_node
            current = new_node
            if i == y-1:
                if future_node == None:
                    self.tail = current
                current.next = future_node

    def delete(self, x, y):
        if x == 0:
            node_after_cut = self.head
            for _ in range(y):
                node_after_cut = node_after_cut.next
            self.head = node_after_cut
            if self.head == None:
                self.tail = None
            return
        else:
            current = self.head
            for _ in range(x-1):
                current = current.next
            node_after_cut = current.next
            for _ in range(y):
                node_after_cut = node_after_cut.next
            current.next = node_after_cut
            if node_after_cut == None:
                self.tail = current

    def get_first_10(self):
        result = []
        current = self.head
        for _ in range(10):
            if current != None:
                result.append(current.value)
                current = current.next
        return result

for t in range(1, 11):
    num_of_pass = int(input())
    ori_pass = list(map(int, input().split()))
    num_of_orders = int(input())
    orders = list(input().split())
    index = 0
    my_list = LinkedList()
    my_list.append(num_of_pass, ori_pass)
    while index < len(orders):
        command = orders[index]
        if command == 'I':
            x = int(orders[index + 1])
            y = int(orders[index + 2])
            s = orders[index + 3:index + 3 + y]
            my_list.insert(x, y, s)
            index += 3 + y
        if command == 'D':
            x = int(orders[index + 1])
            y = int(orders[index + 2])
            my_list.delete(x, y)
            index += 3
        if command == 'A':
            y = int(orders[index + 1])
            s = orders[index + 2:index + 2 + y]
            my_list.append(y, s)
            index += 2 + y
    ans = my_list.get_first_10()
    print(f'#{t}', *ans)