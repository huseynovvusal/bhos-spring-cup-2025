def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False

    return True

def reverse_number(n):
    return int(str(n)[::-1])

def count_mirror_primes(a, b):
    count = 0

    for num in range(a, b + 1):
        if is_prime(num):
            reversed_num = reverse_number(num)
    
            if is_prime(reversed_num):
                count += 1
    
    return count

a, b = map(int, input().split())

print(count_mirror_primes(a, b))
