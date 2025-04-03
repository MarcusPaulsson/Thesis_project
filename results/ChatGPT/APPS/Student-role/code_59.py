def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        
        # Find the minimum and maximum of the known values
        known_values = [x for x in a if x != -1]
        min_known = min(known_values)
        max_known = max(known_values)
        
        # If no known values, we can choose k freely, let's say 0
        if not known_values:
            results.append("0 0")
            continue
        
        # The minimum possible value of m
        m = max(max_known - min_known, abs(min_known - 0), abs(max_known - 0))
        
        # The optimal k
        k = (min_known + max_known) // 2
        
        results.append(f"{m} {k}")
    
    print("\n".join(results))

solve()