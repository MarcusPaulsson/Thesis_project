def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_1 = a.index(1)
    pos_n = a.index(n)

    ans = 0
    
    # Try swapping 1 with the element at the beginning
    ans = max(ans, abs(0 - pos_n))
    
    # Try swapping 1 with the element at the end
    ans = max(ans, abs(n - 1 - pos_n))
    
    # Try swapping n with the element at the beginning
    ans = max(ans, abs(0- pos_1))
    
    # Try swapping n with the element at the end
    ans = max(ans, abs(n-1- pos_1))
    
    print(ans)

solve()