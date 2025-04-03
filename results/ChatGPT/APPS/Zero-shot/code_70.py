def min_replacements_to_k_complete(t, test_cases):
    results = []
    for n, k, s in test_cases:
        m = n // k
        changes = 0
        
        # For each group of k characters
        for j in range(k):
            # Count frequency of characters in the j-th position of each block
            freq = {}
            for i in range(m):
                char = s[j + i * k]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            
            # Calculate the number of changes needed
            max_freq = max(freq.values(), default=0)
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

# Get results and print them
output = min_replacements_to_k_complete(t, test_cases)
print('\n'.join(map(str, output)))