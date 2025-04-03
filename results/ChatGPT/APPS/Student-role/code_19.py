def check_records(test_cases):
    results = []
    for _ in range(test_cases):
        n = int(input())
        prev_p, prev_c = 0, 0
        valid = True
        
        for _ in range(n):
            p, c = map(int, input().split())
            if p < prev_p or c < prev_c or c > p:
                valid = False
            if p - prev_p < c - prev_c:
                valid = False
            prev_p, prev_c = p, c
        
        results.append("YES" if valid else "NO")
    
    return results

# Input handling
T = int(input())
results = check_records(T)
for result in results:
    print(result)