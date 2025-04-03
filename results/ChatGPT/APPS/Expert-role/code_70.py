def min_replacements_to_k_complete(t, test_cases):
    results = []
    for n, k, s in test_cases:
        m = n // k
        replacements = 0
        
        for j in range(k):
            count = [0] * 26  # Count occurrences of each character in this group
            for i in range(m):
                count[ord(s[j + i * k]) - ord('a')] += 1
            
            # Calculate the minimum changes needed to make the characters in this group the same
            max_count = max(count)
            replacements += m - max_count
        
        results.append(replacements)

    return results

# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, 2 * t, 2):
    n, k = map(int, data[i].split())
    s = data[i + 1]
    test_cases.append((n, k, s))

results = min_replacements_to_k_complete(t, test_cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')