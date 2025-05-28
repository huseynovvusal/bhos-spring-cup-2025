# I. Count Subarrays

## 📝 Problem

Given a permutation P of length N, for each integer i where 1 ≤ i ≤ N, find the number of subarrays of P with sum equal to i.

> **Key Definition**: In a permutation of length N, each integer from 1 to N appears exactly once.

## 🧠 Problem Analysis

This problem asks us to count subarrays with specific sums in a permutation. Since we're working with a permutation, each value from 1 to N appears exactly once, which gives us some useful properties:

1. All values in the permutation are positive, so the sum of a subarray always increases as we add more elements.
2. The smallest possible sum is 1 (when the subarray contains just the element with value 1).
3. The largest possible sum could be much larger than N, but we only need to count subarrays with sums between 1 and N.

### Example:

For permutation [3, 1, 2]:

- Subarrays: [3], [1], [2], [3,1], [1,2], [3,1,2]
- Sums: 3, 1, 2, 4, 3, 6
- For i=1: Count=1 ([1])
- For i=2: Count=1 ([2])
- For i=3: Count=2 ([3] and [1,2])

## 💡 Solution Approach

1. **Generate all possible subarrays** of the permutation
2. **For each subarray**, calculate its sum
3. **Increment the counter** for the corresponding sum if it's within the range 1 to N

We can efficiently generate all subarrays using two nested loops:

- The outer loop selects the starting index
- The inner loop extends the subarray by adding elements from the right

## 🔑 Key Steps

1. **Initialize an array to store results**:

   - Create an array of size N with all values initialized to 0
   - Each index i-1 will store the count of subarrays with sum i

2. **Generate all subarrays and count by sum**:

   - Use an outer loop to iterate through all possible starting positions
   - For each starting position, use an inner loop to extend the subarray
   - Keep a running sum as elements are added to the subarray
   - If the sum is between 1 and N, increment the corresponding counter
   - Break the inner loop if the sum exceeds N (optimization)

3. **Output the results**:
   - Print the counts for all sums from 1 to N

## ⏱️ Complexity

- **Time**: $O(N^2)$ in the worst case - we potentially check all subarrays
- **Space**: $O(N)$ - we store N counters for sums 1 through N

## 💻 Full Solution

```python
def solve():
    # Read the size of the permutation
    n = int(input())
    # Read the permutation elements
    a = list(map(int, input().split()))

    # Initialize array to count subarrays for each sum (1 to n)
    ans = [0] * n
    # Start with the first element
    i = 0

    # Iterate through all possible starting positions
    while i < n:
        # Initialize current sum with first element of subarray
        curr = a[i]

        # Check if the single element forms a valid subarray with sum <= n
        if curr <= n:
            # Increment count for sum = curr (using 0-based indexing)
            ans[curr - 1] += 1

        # Initialize index for the next element in subarray
        j = i + 1

        # Extend the subarray by including more elements
        while j < n:
            # Add next element to current sum
            curr += a[j]

            # Optimization: stop if sum exceeds n (we only track sums 1 to n)
            if curr > n: break

            # Increment count for the current sum
            ans[curr - 1] += 1
            # Move to next element
            j += 1

        # Move to next starting position
        i += 1

    # Print the counts for all sums from 1 to n
    for i in range(n):
        print(ans[i], end=" ")
    print()

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    solve()
```

The solution efficiently counts subarrays with specific sums by:

1. **Optimizing the search space**:

   - We only consider subarrays with sums $\leq{N}$
   - We stop extending a subarray once its sum exceeds N

2. **Direct indexing**:

   - The result array is 0-indexed, so we use ans[curr-1] to count subarrays with sum curr

3. **Handling multiple test cases**:
   - The solution resets the counter array for each test case
