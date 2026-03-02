def insert(x, y, s):
    global index
    x_int = int(x)
    y_int = int(y)
    for i in range(y_int):
        original_pass.insert(x_int,s[i])
        x_int += 1

def delete(x, y):
    global index
    x_int = int(x)
    y_int = int(y)
    for i in range(y_int):
        original_pass.pop(x_int)

def append(y, s):
    original_pass.extend(s)

for t in range(1, 11):
    N = int(input())
    original_pass = list(map(int, input().split()))
    num_orders = int(input())
    orders = list(input().split())
    index = 0
    while index < len(orders):
        command = orders[index]
        if command == 'I':
            x = orders[index+1]
            y = int(orders[index+2])
            s = orders[index+3:index+3+y]
            insert(x,y,s)
            index += 3 + y
        if command == 'D':
            x = orders[index + 1]
            y = int(orders[index + 2])
            delete(x, y)
            index += 3
        if command == 'A':
            y = int(orders[index+1])
            s = orders[index+2:index+2+y]
            append(y,s)
            index += 2 + y
    print(f'#{t}', *original_pass[:10])