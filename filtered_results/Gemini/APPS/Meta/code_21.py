def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = 0
    
    # Try swapping min with first element
    temp_a = a[:]
    temp_a[0], temp_a[pos_min] = temp_a[pos_min], temp_a[0]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    # Try swapping min with last element
    temp_a = a[:]
    temp_a[-1], temp_a[pos_min] = temp_a[pos_min], temp_a[-1]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    # Try swapping max with first element
    temp_a = a[:]
    temp_a[0], temp_a[pos_max] = temp_a[pos_max], temp_a[0]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    # Try swapping max with last element
    temp_a = a[:]
    temp_a[-1], temp_a[pos_max] = temp_a[pos_max], temp_a[-1]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    print(ans)
solve()