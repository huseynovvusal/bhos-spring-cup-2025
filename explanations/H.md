# H. Prize-Winning Pairs

## 📝 Problem

Given an array A of length N, find how many pairs of indices (i,j) where $1 \leq i \leq N$ satisfy the condition that a, b, and c form an arithmetic progression where:

- a = $A_i - A_j$
- b = $A_i + A_j$
- c = $A_i × A_j$

> **Key Constraint**: The values a, b, c must form an arithmetic progression.

## 🧠 Problem Analysis

For three numbers to form an arithmetic progression, the difference between consecutive terms must be equal.

$$b - a = c - b$$

Substituting our formulas:

- $(A_i + A_j) - (A_i - A_j) = (A_i × A_j) - (A_i + A_j)$

Simplifying:

- $2A_j = (A_i × A_j) - (A_i + A_j)$
- $2A_j = A_i × A_j - A_i - A_j$
- $2A_j + A_j = A_i × A_j - A_i$
- $3A_j = A_i × A_j - A_i$
- $3A_j = A_i(A_j - 1)$
- $3 = A_i(A_j - 1)/A_j$
- $3 = A_i - A_i/A_j$

Solving for $A_i$:

- $A_i(1 - 1/A_j) = 3$
- $A_i = 3/(1 - 1/A_j)$
- $A_i = 3A_j/(A_j - 1)$

Therefore, for a pair (i, j) to satisfy our condition, the following must be true:

- $A_i = 3A_j/(A_j - 1)$ for $A_j > 1$
- If $A_j = 1$, there's no valid $A_i$

This can be rewritten as:

- $A_i(A_j - 1) = 3A_j$
- $A_i × A_j - A_i = 3A_j$
- $A_i × A_j = 3A_j + A_i$
- $A_i × A_j - 3A_j - A_i = 0$

### Special Cases:

Looking at our formula $A_i = 3A_j/(A_j - 1)$:

- For $A_j = 2$, $A_i = 6$
- For $A_j = 3$, $A_i = 4.5$ (not an integer)
- For $A_j = 4$, $A_i = 4$

So pairs like (6,2) and (4,4) can satisfy our condition.

### Example:

For pair (6, 2) where $A_i = 6$ and $A_j = 2$:

- a = $A_i - A_j = 6 - 2 = 4$
- b = $A_i + A_j = 6 + 2 = 8$
- c = $A_i × A_j = 6 × 2 = 12$

And 8 - 4 = 12 - 8 = 4, so they form an arithmetic progression.

## 💡 Solution Approach

1. **For each potential $A_j$ value**, calculate the corresponding $A_i$ value using the formula $A_i = 3A_j/(A_j - 1)$
2. **Check if the calculated $A_i$ is a valid integer** in our array
3. **Count the number of such pairs**

Since the array can contain duplicate elements, we need to be careful with counting.

## 🔑 Key Steps

1. Create a frequency counter for all numbers in the array
2. For each possible value $A_j$ in the array:
   - Skip if $A_j = 1$ (would cause division by zero)
   - Calculate the required $A_i = 3A_j/(A_j - 1)$
   - If $A_i$ is an integer and exists in our array, count the valid pairs
3. For special case where $A_i = A_j$ (like when $A_j = 4$):
   - Count combinations of 2 different positions from the same number
4. For cases where $A_i \neq A_j$:
   - Count all possible pairs by multiplying their frequencies

## ⏱️ Complexity

- **Time**: $O(N)$ - we only need to process each unique number in the array once
- **Space**: $O(N)$ - to store the frequency count of each number

## 💻 Mathematical Derivation and Solution Analysis

The key insight in this problem is to find when a, b, c form an arithmetic progression. In an arithmetic progression, the difference between consecutive terms is constant.

$$b - a = c - b$$

Substituting the given formulas:

- $(A_i + A_j) - (A_i - A_j) = (A_i × A_j) - (A_i + A_j)$
- $2A_j = A_i × A_j - A_i - A_j$
- $3A_j = A_i × A_j - A_i$
- $3A_j = A_i(A_j - 1)$
- $A_i = 3A_j/(A_j - 1)$

This formula tells us that for each $A_j$, there's at most one possible value of $A_i$ that can form an arithmetic progression. We need to:

1. Ensure $A_j ≠ 1$ to avoid division by zero
2. Check if $3A_j/(A_j - 1)$ is an integer
3. Verify if this integer exists in our array

Our solution counts all such valid pairs efficiently using a frequency counter approach.

## 🔍 Full Solution

```python
def solve():
    # Read the size of the array
    n = int(input())
    # Read array elements
    arr = list(map(int, input().split()))
    # Dictionary to track frequency of each number
    d = {}
    # Initialize result counter
    res = 0

    # Process array in reverse order to ensure we only count pairs (i,j) where i appears after j
    for a in reversed(arr):
        # Special case: When a = 4, pairs with previous 4's form valid arithmetic progressions
        # Since for Aj = 4, Ai = 3*4/(4-1) = 4
        if a == 4:
            # Count pairs with previous 4's
            res += d.get(4, 0)

        # Special case: When a = 6, pairs with 2's form valid arithmetic progressions
        # Since for Aj = 2, Ai = 3*2/(2-1) = 6
        elif a == 6:
            # Count pairs with previous 2's
            res += d.get(2, 0)

        # Update frequency count for current element
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    # Output the result
    print(res)

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    solve()
```
