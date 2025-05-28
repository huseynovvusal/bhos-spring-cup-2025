# D. Aydan's Problem

## 📝 Problem

Given $n$ events with start times $a$ and end times $b$, find the maximum number of events that can be fully attended without overlap.

> **Key Constraint**: Events cannot overlap - a new event can only start after the previous one ends.

## 💡 Solution Approach

1. **Sort events** by their end times (greedy approach)
2. **Process events** in order, selecting those that don't conflict
3. **Keep track** of the latest end time of selected events

## 🔑 Key Steps

```python
# 1. Sort events by end time (earlier ending events first)
intervals.sort(key=lambda x: x[1])

# 2. Process events greedily
count = 0
current_end = 0

for start, end in intervals:
    # If current event starts after previous event ends, select it
    if current_end <= start:
        current_end = end
        count += 1
```

## ⏱️ Complexity

- **Time**: $O(n \log n)$ - dominated by sorting
- **Space**: $O(n)$ - to store the intervals

## 💻 Full Solution

```python
# Read the number of events
n = int(input())

# Store all events as (start_time, end_time) pairs
intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))

# Sort events by end time (greedy approach)
intervals.sort(key=lambda x: x[1])

count = 0
current_end = 0

# Process events in order of end time
for start, end in intervals:
    # If this event starts after or at the same time the previous event ends
    if current_end <= start:
        # Select this event and update current end time
        current_end = end
        count += 1

# Print the maximum number of events that can be attended
print(count)
```
