import sys

N = int(sys.stdin.readline())
primes = [True] * (N+1)
primes[0], primes[1] = False, False
for i in range(2, int(N ** 0.5)+1):
    if primes[i]:
        for j in range(i * i, N+1, i):
            primes[j] = False
res = [i for i in range(2, N + 1) if primes[i]]
left, right = 0, 0
count = 0
add_res = 0
while True:
    if add_res >= N:
        if add_res == N:
            count +=1
        add_res -= res[left]
        left += 1
    elif right == len(res):
        break
    else:
        add_res += res[right]
        right += 1
print(count)