def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = 0
    
    # Case 1: No swap
    ans = max(ans, abs(pos_min - pos_max))

    # Case 2: Swap min with first element
    ans = max(ans, abs(0 - pos_max))
    
    # Case 3: Swap min with last element
    ans = max(ans, abs(n - 1 - pos_max))
    
    # Case 4: Swap max with first element
    ans = max(ans, abs(pos_min - 0))
    
    # Case 5: Swap max with last element
    ans = max(ans, abs(pos_min - (n - 1)))
    
    
    print(ans)

solve()