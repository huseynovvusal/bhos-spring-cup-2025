def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = [0] * n
    i = 0
    
    while i < n:
        curr = a[i]
        
        if curr <= n:
            ans[curr - 1] += 1
        
        j = i + 1

        while j < n:
            curr += a[j]
        
            if curr > n: break
        
            ans[curr - 1] += 1
            j += 1
        
        i += 1
    
    for i in range(n):
        print(ans[i], end=" ")
    print()

t = int(input())

for _ in range(t):
    solve()