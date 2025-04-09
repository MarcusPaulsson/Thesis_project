def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 2:
        print(0)
        return

    min_instability = float('inf')
    
    # Try removing each element and calculate instability
    for i in range(n):
        temp_a = a[:i] + a[i+1:]
        min_val = min(temp_a)
        max_val = max(temp_a)
        instability = max_val - min_val
        min_instability = min(min_instability, instability)

    print(min_instability)

solve()