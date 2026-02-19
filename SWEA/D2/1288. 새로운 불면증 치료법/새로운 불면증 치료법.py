T = int(input())
total = (1 << 10) - 1

for t in range(1, T+1):
    N = int(input())
    visited = 0
    multiple = 0
    condition = True
    while condition:
        multiple += 1
        str_num = str(N * multiple)
        for char in str_num:
            num_char = int(char)
            visited = visited | (1 << num_char)
        if total == visited:
            print(f'#{t} {str_num}')
            condition = False