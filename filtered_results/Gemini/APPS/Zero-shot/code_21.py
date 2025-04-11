def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = 0
    
    # Case 1: Swap with the first element
    temp_a = a[:]
    temp_a[0], temp_a[pos_min] = temp_a[pos_min], temp_a[0]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    temp_a = a[:]
    temp_a[0], temp_a[pos_max] = temp_a[pos_max], temp_a[0]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

    # Case 2: Swap with the last element
    temp_a = a[:]
    temp_a[-1], temp_a[pos_min] = temp_a[pos_min], temp_a[-1]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
    temp_a = a[:]
    temp_a[-1], temp_a[pos_max] = temp_a[pos_max], temp_a[-1]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

    print(ans)

solve()