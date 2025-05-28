# B. Colored Boxes

## 📝 Problem

Calculate the number of ways to paint $N$ boxes with 3 colors (red, yellow, and green) such that no two adjacent boxes have the same color, where $1 \leq N \leq 50$.

> **Key Constraint**: No two adjacent boxes can have the same color.

## 💡 Solution Approach

1. **Analyze the pattern**: For each box after the first, we can use only 2 of the 3 colors
2. **Apply combinatorial logic**: First box has 3 choices, each subsequent box has 2 choices
3. **Calculate**: $3 \times 2^{N-1}$ gives the total number of valid colorings

## 🔑 Key Steps

1. **Analyze the coloring constraints**:

   - For the first box, we can use any of the 3 colors (red, yellow, green)
   - For each subsequent box, we cannot use the same color as the adjacent box
   - This means each box after the first has 2 possible color choices

2. **Apply the multiplication principle**:

   - First box: 3 choices
   - Each of the remaining (N-1) boxes: 2 choices each
   - Total number of ways: 3 × 2^(N-1)

3. **Calculate the result**:
   - Use modular exponentiation for large values of N if needed
   - Return the final count of valid colorings

## ⏱️ Complexity

- **Time**: $O(1)$ - direct formula calculation regardless of input size
- **Space**: $O(1)$ - constant additional space regardless of input size

## 💻 Full Solution

```python
n = int(input())

# Formula: 3 * 2^(n-1)
# - First box: 3 choices
# - Each subsequent box: 2 choices (can't use previous color)
print(3 * (2 ** (n - 1)))
```
