import heapq
import sys

input = sys.stdin.readline
N = int(input())
boo = []
heapq.heapify(boo)
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(boo) == 0:
            print(0)
        else:
            print(-heapq.heappop(boo))
    else:
        heapq.heappush(boo, -x)