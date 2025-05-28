# G. Classification of Mushrooms

## 📝 Problem

Divide $n$ mushrooms into two groups such that the difference between the total weights of the two groups is minimized.

> **Key Objective**: Minimize $|sum(group1) - sum(group2)|$ where all mushrooms must be used.

## 🧠 Problem Analysis

This is a variant of the **Partition Problem** (a special case of the subset sum problem), which is NP-hard. However, given the constraint that $n \leq 20$, a recursive approach with exponential time complexity is feasible.

For each mushroom, we have two choices:

1. Put it in group 1
2. Put it in group 2

By trying all possible combinations and tracking the minimum difference, we can find the optimal solution.

### Example:

For mushrooms with weights [3, 2, 7, 4, 1]:

The optimal division is:

- Group 1: [2, 3, 4] with total weight 9
- Group 2: [7, 1] with total weight 8

The difference is |9 - 8| = 1, which is minimal.

## 💡 Solution Approach

1. **Use recursion** to try all possible ways to divide mushrooms
2. **For each mushroom**, consider adding it to either group 1 or group 2
3. **Track running sums** for both groups
4. **Return the minimum difference** found after placing all mushrooms

## 🔑 Key Steps

1. **Define a recursive approach**:

   - Create a function that processes one mushroom at a time
   - Track the running sum of weights for both groups
   - Use index parameter to keep track of which mushroom is being processed

2. **Implement the decision process**:

   - For each mushroom, consider adding it to either group 1 or group 2
   - Make two recursive calls representing both choices
   - Take the minimum result from both decisions

3. **Handle the base case**:

   - When all mushrooms have been assigned (index reaches n)
   - Calculate and return the absolute difference between group sums

4. **Optimize if needed**:
   - For larger inputs, consider using memoization to avoid redundant calculations
   - Dynamic programming approach would store results of subproblems

## ⏱️ Complexity

- **Time**: $O(2^n)$ - we make two recursive calls for each of the n mushrooms
- **Space**: $O(n)$ - maximum recursion depth is n

## 💻 Full Solution

```python
# Read the number of mushrooms
n = int(input())

# Read the weights of the mushrooms
weights = list(map(int, input().split()))

# Recursive function to find minimum weight difference
def recurse_apples(weights, i = 0, sum1 = 0, sum2 = 0):
	# Base case: all mushrooms have been placed in groups
	if i == n:
		return abs(sum2 - sum1)  # Return the absolute difference

	# Try both possibilities and return the minimum:
	return min(
		# Option 1: Add current mushroom to group 1
		recurse_apples(weights, i + 1, sum1 + weights[i], sum2),

		# Option 2: Add current mushroom to group 2
		recurse_apples(weights, i + 1, sum1, sum2 + weights[i]),
	)

# Print the minimum possible difference
print(recurse_apples(weights))
```
