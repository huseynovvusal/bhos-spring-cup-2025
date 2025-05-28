# A. "Mirror Prime" Numbers

## 📝 Problem

Count the number of "mirror primes" in range $[a,b]$ where $1 \leq a \leq b \leq 10000$.

> **Mirror Prime**: A number that is prime, and when its digits are reversed, the resulting number is also prime.

## 💡 Solution Approach

1. **Check primality** of each number in range
2. For primes, **reverse the digits** and check primality again
3. **Count** numbers that satisfy both conditions

## 🔑 Key Steps

```python
# 1. Check if number is prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 2. Reverse digits
def reverse_number(n):
    return int(str(n)[::-1])

# 3. Count mirror primes
def count_mirror_primes(a, b):
    return sum(1 for num in range(a, b + 1)
              if is_prime(num) and is_prime(reverse_number(num)))
```

## ⏱️ Complexity

- **Time**: $O((b-a)\sqrt{b})$
- **Space**: $O(1)$

## 💻 Full Solution

```python
# Problem A: Mirror Primes
# A "mirror prime" is a number that is:
# 1) Prime itself
# 2) When its digits are reversed, that number is also prime

def is_prime(n):
    # Numbers less than 2 are not prime by definition
    if n < 2:
        return False

    # Check divisibility up to square root of n (optimization)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False

    # If no divisors found, n is prime
    return True

def reverse_number(n):
    # Convert to string, reverse, then convert back to integer
    return int(str(n)[::-1])

def count_mirror_primes(a, b):
    count = 0

    # Check each number in the range [a, b]
    for num in range(a, b + 1):
        # First check if number is prime
        if is_prime(num):
            # If prime, check if its reverse is also prime
            reversed_num = reverse_number(num)

            if is_prime(reversed_num):
                count += 1

    return count

# Read input: two integers a and b (1 ≤ a ≤ b ≤ 10000)
a, b = map(int, input().split())

# Print the count of mirror primes in range [a, b]
print(count_mirror_primes(a, b))

# Examples:
# 11 is prime and reverse(11) = 11 is also prime → mirror prime
# 13 is prime and reverse(13) = 31 is also prime → mirror prime
# 17 is prime and reverse(17) = 71 is also prime → mirror prime
```
