# F. Ribbons

## 📝 Problem

Given $n$ ribbons of various lengths, cut them to obtain exactly $k$ ribbons of equal length. Find the maximum possible length of these equal segments.

> **Key Constraint**: All segments must have the same integer length, and we need exactly $k$ such segments.

## 🧠 Problem Analysis

The problem involves finding the maximum possible equal length for the ribbons, which leads to a binary search solution:

1. The minimum possible segment length is 1 cm.
2. The maximum possible segment length cannot be greater than the longest ribbon.
3. For any given segment length $x$:
   - From a ribbon of length $L$, we can cut $\lfloor L/x \rfloor$ segments of length $x$.
   - The total number of segments is the sum across all ribbons.

Binary search allows us to efficiently narrow down the optimal length by checking whether we can make at least $k$ segments for a given length. If yes, we try larger lengths; if no, we try smaller lengths.

### Example:

For ribbons of lengths [802, 743, 457, 539] and k = 11:

- For length = 200:

  - 802 ÷ 200 = 4 segments
  - 743 ÷ 200 = 3 segments
  - 457 ÷ 200 = 2 segments
  - 539 ÷ 200 = 2 segments
  - Total: 11 segments ✓

- For length = 201:
  - Total: 10 segments ✗

Therefore, 200 is the maximum possible segment length.

## 💡 Solution Approach

1. **Use binary search** to find the maximum possible length
2. **For each potential length**, calculate how many segments can be obtained
3. **Find the largest value** for which we can get at least $k$ segments

## 🔑 Key Steps

```python
# 1. Set up binary search boundaries
left = 1                 # Minimum possible length (1 cm)
right = max(lengths)     # Maximum possible length

# 2. Perform binary search for optimal segment length
while left <= right:
    mid = (left + right) // 2

    # Count how many segments of length mid we can make
    count = sum(l // mid for l in lengths)

    if count >= k:
        # We can make at least k segments, try for larger length
        result = mid
        left = mid + 1
    else:
        # Can't make k segments, try smaller length
        right = mid - 1
```

## ⏱️ Complexity

- **Time**: $O(n \log L)$ - where $L$ is the maximum ribbon length and $n$ is the number of ribbons
- **Space**: $O(n)$ - to store the lengths of the ribbons

## 💻 Full Solution

```python
def max_segment_length(k, lengths):
    # Initialize binary search boundaries
    left = 1                 # Minimum possible segment length
    right = max(lengths)     # Maximum possible segment length
    result = 0               # Store the best result found

    # Binary search for the maximum possible segment length
    while left <= right:
        mid = (left + right) // 2

        # Calculate how many segments of length 'mid' we can cut
        count = sum(l // mid for l in lengths)

        if count >= k:
            # If we can cut at least k segments, this length works
            # Store it and try for even larger lengths
            result = mid
            left = mid + 1
        else:
            # If we can't cut k segments, try smaller lengths
            right = mid - 1

    return result

# Read input
n, k = map(int, input().split())
lengths = [int(input()) for _ in range(n)]

# Print the maximum possible segment length
print(max_segment_length(k, lengths))
```
