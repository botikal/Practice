N = int(input())
board = [[0] * N for _ in range(N)]
glb_cnt = 0

col_used = [False] * N
diag1_used = [False] * (2 * N - 1)   # row+col index
diag2_used = [False] * (2 * N - 1)   # row-col+N-1 index

def N_Queens(row):
    global glb_cnt
    if row == N:
        glb_cnt += 1
        return
    for col in range(N):
        if col_used[col] or diag1_used[row+col] or diag2_used[row-col+N-1]:
            continue
        board[row][col] = 1
        col_used[col] = diag1_used[row+col] = diag2_used[row-col+N-1] = True

        N_Queens(row + 1)

        board[row][col] = 0
        col_used[col] = diag1_used[row+col] = diag2_used[row-col+N-1] = False

N_Queens(0)
print(glb_cnt)
