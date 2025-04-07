def solve():
    n, m, k = map(int, input().split())
    
    table = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            table.append(i * j)
    
    table.sort()
    
    print(table[k - 1])

solve()