T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    hash_table = {i:[] for i in range(10000)}
    n_set = list(input().split())
    for word in n_set:
        string_val = hash(word) % 10000
        hash_table[string_val].append(word)
    m_set = list(input().split())
    for word in m_set:
        string_val = hash(word) % 10000
        if word in hash_table[string_val]:
            ans += 1
    print(f'#{t} {ans}')