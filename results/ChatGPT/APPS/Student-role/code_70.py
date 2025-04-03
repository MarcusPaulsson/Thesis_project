def min_replacements_to_k_complete(t, test_cases):
    results = []
    for n, k, s in test_cases:
        # Number of groups based on period k
        groups = n // k
        # To count replacements needed
        replacements = 0
        
        # Each position in the first half of the k-period
        for i in range((k + 1) // 2):
            # Count frequency of characters in the corresponding positions
            freq = {}
            for j in range(groups):
                # Positions to consider
                positions = [j * k + i, j * k + (k - 1 - i)]
                for pos in positions:
                    if pos < n:
                        char = s[pos]
                        if char in freq:
                            freq[char] += 1
                        else:
                            freq[char] = 1
            
            # Total characters in these positions
            total = sum(freq.values())
            # Max frequency of a single character
            max_freq = max(freq.values(), default=0)
            # Replacements needed for this set of positions
            replacements += total - max_freq
            
        results.append(replacements)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])  # Number of test cases
test_cases = []
for i in range(1, 2 * t, 2):
    n, k = map(int, data[i].split())
    s = data[i + 1]
    test_cases.append((n, k, s))

# Get results
results = min_replacements_to_k_complete(t, test_cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')