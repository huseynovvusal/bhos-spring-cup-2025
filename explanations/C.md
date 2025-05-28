# C. Square of Maximum Number

## 📝 Problem

For a given three-digit number, rearrange its digits to form the largest possible number, then calculate and print the square of that number.

> **Key Operation**: Maximize the number by sorting digits in descending order, then calculate its square.

## 💡 Solution Approach

1. **Extract digits** from the input number
2. **Sort digits** in descending order to create the largest possible number
3. **Square the result** and print the answer

## 🔑 Key Steps

1. **Extract and process input**:

   - Read the three-digit number as a string
   - Convert the string to individual characters

2. **Rearrange to find maximum number**:

   - Sort the digits in descending order
   - Join the sorted digits into a new string
   - Convert the string back to an integer

3. **Calculate the result**:
   - Square the rearranged number
   - Return the final value

## ⏱️ Complexity

- **Time**: $O(1)$ - sorting a fixed number of digits (3 digits)
- **Space**: $O(1)$ - constant additional space regardless of input size

## 💻 Full Solution

```python
# Read input, sort digits in descending order, convert back to integer
n = int("".join(sorted(input(), reverse = True)))

# Square the result and print
print(n ** 2)
```
