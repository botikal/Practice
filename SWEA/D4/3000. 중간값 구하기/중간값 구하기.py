import heapq

T = int(input())
for t in range(1, T + 1):
    N, A = map(int, input().split())
    total = 0
    max_heap = [-A]
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for i in range(N):
        new_nums = list(map(int,input().split()))
        for j in range(2):
            heapq.heappush(max_heap, -new_nums[j])
            temp = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -temp)
            if len(min_heap) > len(max_heap):
                move_temp = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -move_temp)
        temp_med = -1 * max_heap[0]
        total += temp_med % 20171109
    total %= 20171109
    print(f'#{t} {total}')