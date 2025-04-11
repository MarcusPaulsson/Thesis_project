def solve():
    a = int(input())
    
    if a == 1:
        print(1)
        return

    n = 0
    while (1 << n) <= a:
        n += 1
    
    print(n - 1)

solve()