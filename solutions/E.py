def solve():
    n = int(input())

    res = [[0] * n for _ in range(n)]

    num = 1

    for _i in range(n):
        for _j in range(n):
            i = _i
            j = _j

            if(res[i][j] != 0): continue 

            while(0 <= i < n and 0 <= j < n):
                res[i][j] = num
                num += 1
                i += 1
                j -= 1


    for row in res:
        print(*row)

for i in range(int(input())):
    solve()