import sys

def cantor(N, base, l, r):
    if N == 0:
        return
    mid = (r - l) // 3
    for i in range(l + mid,l + 2 * mid):
        base[i] = ' '
    cantor(N-1, base, l,l + mid)
    cantor(N-1, base, l + 2 * mid, r)
for lin in sys.stdin:
    T = int(lin.strip())
    start = ['-'] * (3 ** T)

    cantor(T, start, 0, len(start))

    print(''.join(start))