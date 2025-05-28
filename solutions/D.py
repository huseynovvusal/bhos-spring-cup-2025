n = int(input())

intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))

intervals.sort(key=lambda x: x[1])

count = 0
current_end = 0

for start, end in intervals:
    if current_end <= start:
        current_end = end
        count += 1

print(count)
