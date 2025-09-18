N = int(input())
mat = [['*'] * N for _ in range(N)]

def stars(y, x, size):
    if size == 1:
        return
    third = size//3
    for dy in range(y + third,y + 2 * third):
        for dx in range(x + third, x + 2 * third):
            mat[dy][dx] = ' '
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            stars(y + i*third,x + j * third, third)

stars(0,0, N)
ans_str = ''
for i in range(N):
    line = ''.join(mat[i])
    ans_str += line + '\n'
print(ans_str)