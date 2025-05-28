def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    res = 0
    
    for a in reversed(arr):
        if a == 4:
            res += d.get(4, 0)
        elif a == 6:
            res += d.get(2, 0)
            
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    
    print(res)

t = int(input())

for _ in range(t):
    solve()
