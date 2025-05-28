# E. Pattern

## 📝 Problem

Generate an $N \times N$ matrix with numbers 1 to $N^2$ filled in anti-diagonal pattern.

> **Key Pattern**: Numbers are filled along anti-diagonals from bottom-left to top-right.

## 💡 Solution Approach

1. **Initialize** an $N \times N$ matrix with zeros
2. **Traverse** the matrix and fill empty cells along anti-diagonals
3. **Print** the resulting matrix

## 🔑 Key Steps

1. **Initialize the matrix**:

   - Create an N×N matrix filled with zeros
   - Set a counter variable to 1, which will be used to fill the matrix

2. **Implement the anti-diagonal traversal**:

   - Use nested loops to iterate through each cell as potential starting points
   - For each unvisited cell, trace the entire anti-diagonal from that point
   - Anti-diagonals run from top-right to bottom-left (or down and left)

3. **Fill values along anti-diagonals**:

   - For each starting point, follow the anti-diagonal path
   - Increment row (move down) and decrement column (move left) for each step
   - Fill cells with increasing numbers while staying within matrix boundaries
   - Skip cells that have already been filled

4. **Display the result**:
   - Print the completed matrix in the required format

## ⏱️ Complexity

- **Time**: $O(N^2)$ - we visit each cell in the matrix exactly once
- **Space**: $O(N^2)$ - to store the resulting matrix

## 💻 Full Solution

```python
def solve():
    # Read size of matrix
    n = int(input())

    # Create empty N×N matrix
    res = [[0] * n for _ in range(n)]

    # Start with number 1
    num = 1

    # Traverse matrix cells as starting points for anti-diagonals
    for _i in range(n):
        for _j in range(n):
            i = _i
            j = _j

            # Skip if cell already filled
            if(res[i][j] != 0): continue

            # Fill along anti-diagonal (down and left)
            while(0 <= i < n and 0 <= j < n):
                res[i][j] = num
                num += 1
                i += 1  # Move down
                j -= 1  # Move left


    # Print matrix
    for row in res:
        print(*row)

# Process multiple test cases
for i in range(int(input())):
    solve()
```

## 🔍 Pattern Visualization

For $N=4$, the numbers are filled in this order:

1. Start with anti-diagonal 1: Fill cell [0,0] with 1
2. Next anti-diagonal 2: Fill cells [0,1] with 2 and [1,0] with 3
3. Continue with anti-diagonal 3: Fill cells [0,2], [1,1], [2,0] with 4, 5, 6
4. And so on...

```
Filling order by anti-diagonals:

Diagonal 1:    Diagonal 2:    Diagonal 3:    Diagonal 4:
[0,0]=1        [0,1]=2        [0,2]=4        [0,3]=7
               [1,0]=3        [1,1]=5        [1,2]=8
                              [2,0]=6        [2,1]=9
                                             [3,0]=10

Diagonal 5:    Diagonal 6:    Diagonal 7:
[1,3]=11       [2,3]=14       [3,3]=16
[2,2]=12       [3,2]=15
[3,1]=13
```

Final matrix:

```
 1  2  4  7
 3  5  8 11
 6  9 12 14
10 13 15 16
```
