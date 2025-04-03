def min_replacements_to_k_complete(t, test_cases):
    results = []
    for n, k, s in test_cases:
        # n is divisible by k
        m = n // k
        changes = 0
        
        # Check each group of k characters
        for i in range(k):
            count = {}
            for j in range(m):
                char = s[i + j * k]
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            
            # The most frequent character in this group
            max_freq = max(count.values(), default=0)
            # We need to change the other characters in this group
            changes += (m - max_freq)
        
        results.append(changes)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Get results
results = min_replacements_to_k_complete(t, test_cases)

# Print results
for result in results:
    print(result)