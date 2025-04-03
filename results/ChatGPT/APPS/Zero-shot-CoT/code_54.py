def can_win_game(queries):
    results = []
    for _ in range(queries):
        n = int(input())
        s = list(map(int, input().split()))
        
        # Check if 2048 is already present
        if 2048 in s:
            results.append("YES")
            continue
        
        # Sum all powers of two less than or equal to 2048
        total_sum = sum(x for x in s if x < 2048)
        
        # If the total sum of powers of two is at least 2048, we can achieve it
        if total_sum >= 2048:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input and processing queries
q = int(input())
results = can_win_game(q)
for result in results:
    print(result)