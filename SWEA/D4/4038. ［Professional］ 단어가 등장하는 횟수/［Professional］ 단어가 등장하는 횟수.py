T = int(input())
for t in range(1, T+1):
    B = input()
    B_len = len(B)
    S = input()
    S_len = len(S)
    if S_len > B_len:
        print(f'#{t} 0')
        continue
    base = 256
    modulo = 1000000007

    hash_B = 0
    hash_S = 0
    power = pow(base, S_len-1, modulo)
    for i in range(S_len):
        hash_S = (hash_S * base + ord(S[i])) % modulo
        hash_B = (hash_B * base + ord(B[i])) % modulo
    count = 0

    for i in range(B_len-S_len+1):
        if hash_S == hash_B:
            count += 1
        if i < B_len - S_len:
            hash_B = (hash_B - ord(B[i]) * power)
            hash_B = hash_B * base + ord(B[i+S_len])
            hash_B %= modulo
    print(f'#{t} {count}')