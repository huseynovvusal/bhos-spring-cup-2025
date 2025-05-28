# D. Aydan's Problem

## 📝 Problem

Given $n$ events with start times $a$ and end times $b$, find the maximum number of events that can be fully attended without overlap.

> **Key Constraint**: Events cannot overlap - a new event can only start after the previous one ends.

## 💡 Solution Approach

1. **Sort events** by their end times (greedy approach)
2. **Process events** in order, selecting those that don't conflict
3. **Keep track** of the latest end time of selected events

## 🔑 Key Steps

1. **Prepare the events data**:

   - Store each event as a pair of (start_time, end_time)
   - Sort all events by their end times (greedy approach)

2. **Initialize tracking variables**:

   - Set count of attended events to zero
   - Set current_end to zero (representing the earliest possible start time)

3. **Process events in sorted order**:

   - For each event, check if it starts after the current_end time
   - If compatible (no overlap), include the event and update current_end
   - Continue until all events are processed

4. **Return the result**:
   - The final count represents the maximum number of non-overlapping events

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
