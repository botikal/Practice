def quad(size, pap):
    top_left= pap[0][0]
    med = size//2
    if all(all(cell == top_left for cell in row) for row in pap):
        return str(top_left)
    parts = []
    for y in range(2):
        for x in range(2):
            part = []
            for dy in range(med):
                line_list = []
                for dx in range(med):
                    line_list.append(pap[y * med + dy][x * med + dx])
                part.append(line_list)
            parts.append(quad(med, part))
    return f'({parts[0]}{parts[1]}{parts[2]}{parts[3]})'

N = int(input())
paper = []
for _ in range(N):
    line = list(map(int, input()))
    paper.append(line)
ans = quad(N, paper)
print(ans)