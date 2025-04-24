def has_palindromic_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        index_map = {}
        found = False
        
        for i in range(n):
            if a[i] in index_map:
                # Check if the distance between the same numbers is at least 2
                if i - index_map[a[i]] >= 2:
                    found = True
                    break
            index_map[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

# Read input
t = int(input())
test_cases = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

# Get results
results = has_palindromic_subsequence(test_cases)

# Print results
print("\n".join(results))