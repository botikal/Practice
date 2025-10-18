N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))
scheduled = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        scheduled += 1
        end_time = end
print(scheduled)