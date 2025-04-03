def solve():
    n = int(input())
    a = list(map(int, input().split()))

    bounds = []
    for i in range(n):
        if a[i] == -1:
            if i > 0 and a[i-1] != -1:
                bounds.append(a[i-1])
            if i < n-1 and a[i+1] != -1:
                bounds.append(a[i+1])
    
    if not bounds:
        print(0, 0)
        return

    min_val = min(bounds)
    max_val = max(bounds)
    
    k = (min_val + max_val) // 2
    
    
    def calculate_m(arr, k_val):
        new_arr = [k_val if x == -1 else x for x in arr]
        m = 0
        for i in range(n - 1):
            m = max(m, abs(new_arr[i] - new_arr[i+1]))
        return m
    
    m = calculate_m(a,k)
    
    print(m, k)

t = int(input())
for _ in range(t):
    solve()