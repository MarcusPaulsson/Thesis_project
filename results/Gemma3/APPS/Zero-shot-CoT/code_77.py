def solve():
    n = int(input())
    total_sum = n * (n + 1) // 2
    
    if n % 2 == 0:
        print(1)
    else:
        print(0)

solve()