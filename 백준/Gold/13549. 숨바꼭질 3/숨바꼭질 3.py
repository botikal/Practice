from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
MAX = 100000

dist = [-1] * (MAX + 1)
dq = deque()
dq.append(N)
dist[N] = 0

while dq:
    curr = dq.popleft()
    if curr == K:
        print(dist[curr])
        break
    tele = curr * 2
    if tele <= MAX and (dist[tele] == -1 or dist[tele] > dist[curr]):
        dist[tele] = dist[curr]
        dq.appendleft(tele)
    adv = curr + 1
    if adv <= MAX and (dist[adv] == -1 or dist[adv] > dist[curr] + 1):
        dist[adv] = dist[curr] + 1
        dq.append(adv)
    dec = curr - 1
    if dec >= 0 and (dist[dec] == -1 or dist[dec] > dist[curr] + 1):
        dist[dec] = dist[curr] + 1
        dq.append(dec)