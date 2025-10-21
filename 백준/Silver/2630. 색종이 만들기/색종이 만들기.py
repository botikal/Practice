def cutting_paper(pow, paper):
    global whites, blacks
    first = paper[0][0]
    if all(all(cell == first for cell in row) for row in paper):
        if first == 0:
            whites += 1
        else:
            blacks += 1
        return
    else:
        pow -= 1
        search_range = int(2 ** pow)
        for y in range(2):
            for x in range(2):
                new_paper = []
                for dy in range(search_range):
                    line_list = []
                    for dx in range(search_range):
                        line_list.append(paper[(y * search_range) + dy][(x * search_range) + dx])
                    new_paper.append(line_list)
                cutting_paper(pow, new_paper)

N = int(input())
paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)
power = 0
whites = 0
blacks = 0
for k in range(7, 0, -1):
    if N // (2 ** k) == 1:
        power = k
cutting_paper(power, paper)
print(whites)
print(blacks)