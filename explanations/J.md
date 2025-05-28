# J. Array XOR Queries

## 📝 Problem

Given an array $a_1, a_2, \ldots, a_n$ and $q$ queries of two types:

1. Update: `1 i v` - Change $a_i$ to $v$
2. Query: `2 j k` - Count how many indices $i$ where $i \leq j$ such that $a_1 \oplus a_2 \oplus \ldots \oplus a_i = k$

> **Key Operation**: $\oplus$ represents the XOR (exclusive OR) operation.

## 🧠 Problem Analysis

This problem involves two operations:

1. Updating an element in the array
2. Querying for the count of prefix XORs equal to a given value

A naive approach would recalculate prefix XORs after each update, resulting in $O(n)$ time per update, and $O(j)$ time per query. For large arrays, this approach is too slow.

The key insight is that we can use a **Square Root Decomposition** approach to achieve a better time complexity:

1. Divide the array into blocks of approximately $\sqrt{n}$ size
2. For each block, maintain:
   - Frequency of each prefix XOR value within the block
   - A "block XOR value" that represents changes propagated from previous blocks

### How Updates Affect Prefix XORs

When we update $a_i$ to value $v$, all prefix XORs at positions $\geq i$ are affected. The difference between the new and old value ($a_i \oplus v$) propagates through all subsequent prefix XORs.

### Example:

For array [1, 1, 1, 1, 1] with prefix XORs [1, 0, 1, 0, 1]:

1. Query: Count of prefix XORs equal to 1 up to position 5: Answer is 3 (positions 1, 3, 5)
2. Update: Change $a_3$ from 1 to 2
   - New array: [1, 1, 2, 1, 1]
   - New prefix XORs: [1, 0, 2, 3, 2]
3. Query: Count of prefix XORs equal to 1 up to position 5: Answer is 1 (only position 1)

## 💡 Solution Approach

1. **Square Root Decomposition**:

   - Divide the array into blocks of size approximately $\sqrt{n}$
   - Precompute prefix XORs for the entire array
   - For each block, store frequency of each prefix XOR value

2. **For Update Operations**:

   - Update the array value and calculate the XOR difference
   - Update prefix XORs for the affected block
   - Update block XOR values for all subsequent blocks

3. **For Query Operations**:
   - Count matching prefix XORs in the current block (handling partial blocks)
   - For all previous blocks, count values that XOR with the block's XOR value to give the target

## 🔑 Key Steps

1. **Initialize the data structures**:

   - Create arrays to track block information (start, end, block IDs)
   - Compute prefix XORs for the original array
   - Build square root decomposition with frequency counters for each block

2. **Handle update operations efficiently**:

   - Calculate the XOR difference between old and new values
   - Update prefix XORs in the current block
   - Update frequency counts in the current block
   - Propagate XOR difference to subsequent blocks

3. **Process query operations**:
   - Count matching prefix XORs in the current block up to the query position
   - For all preceding blocks, use frequency counters to find matching prefix XORs
   - Add up all counts to get the final result

## ⏱️ Complexity

- **Time**:
  - Initialization: $O(n)$
  - Update: $O(\sqrt{n})$ per update (worst case)
  - Query: $O(\sqrt{n})$ per query
- **Space**: $O(n + \sqrt{n} \cdot \text{max\_value})$ for storing blocks and frequency dictionaries

## 💻 Full Solution

```python
# Initialize global arrays for square root decomposition
BLOCK_START = [0 for _ in range(1000)]
BLOCK_END = [0 for _ in range(1000)]
BLOCK_XOR = [0 for _ in range(1000)]
BLOCK_ID = [0 for _ in range(10**6 + 100)]
BLOCK_FREQ = [{} for _ in range(1000)]

# Array to store prefix XORs
prefix_xor = [0 for _ in range(10**5 + 10)]

def build_sqrt_decomposition(n):
    # Determine the block size (approximately sqrt(n))
    block_size = 1
    while block_size * block_size < n:
        block_size += 1

    # Divide the array into blocks
    num_blocks = 0
    for i in range(0, n, block_size):
        BLOCK_START[num_blocks] = i
        BLOCK_END[num_blocks] = i + block_size - 1
        num_blocks += 1
    BLOCK_END[num_blocks - 1] = n - 1

    # Initialize block data
    for block in range(num_blocks):
        BLOCK_XOR[block] = 0
        for i in range(BLOCK_START[block], BLOCK_END[block] + 1):
            val = prefix_xor[i]
            BLOCK_FREQ[block][val] = BLOCK_FREQ[block].get(val, 0) + 1
            BLOCK_ID[i] = block

    return block_size

# Read input
n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Compute initial prefix XORs
current_xor = 0
for i in range(n):
    current_xor ^= arr[i]
    prefix_xor[i] = current_xor

# Build the square root decomposition
block_size = build_sqrt_decomposition(n)

# Process queries
for _ in range(q):
    op, index, value = map(int, input().split())
    # Convert to 0-indexed
    index -= 1

    if op == 1:  # Update operation
        # Get the block ID for the index
        block = BLOCK_ID[index]
        # Calculate XOR difference between new and old value
        xor_diff = arr[index] ^ value
        # Update the array
        arr[index] = value

        # Update prefix XORs in the current block
        for j in range(index, BLOCK_END[block] + 1):
            # Remove the old frequency count
            BLOCK_FREQ[block][prefix_xor[j]] -= 1
            # Update the prefix XOR
            prefix_xor[j] ^= xor_diff
            # Update the frequency count
            BLOCK_FREQ[block][prefix_xor[j]] = BLOCK_FREQ[block].get(prefix_xor[j], 0) + 1

        # Propagate XOR difference to subsequent blocks
        for b in range(block + 1, block_size + 1):
            BLOCK_XOR[b] ^= xor_diff

    else:  # Query operation
        # Get the block ID for the index
        block = BLOCK_ID[index]
        count = 0

        # Count within the current block
        for j in range(BLOCK_START[block], index + 1):
            if prefix_xor[j] ^ BLOCK_XOR[block] == value:
                count += 1

        # Count from previous blocks using frequency tables
        for b in range(0, block):
            target = value ^ BLOCK_XOR[b]
            count += BLOCK_FREQ[b].get(target, 0)

        # Print the result
        print(count)
```

The solution efficiently handles both update and query operations using square root decomposition:

1. **Handling prefix XORs**:
   - We use a prefix XOR array to quickly compute XOR of any subarray
   - For any subarray [L,R], the XOR is prefix_xor[R] ^ prefix_xor[L-1]
2. **Efficient updates**:
   - When a value changes, we update the prefix XORs only for the current block
   - For later blocks, we just update a block XOR value
3. **Fast queries**:
   - For the block containing the query index, we scan directly
   - For previous blocks, we use frequency counters to get counts in O(1) time
