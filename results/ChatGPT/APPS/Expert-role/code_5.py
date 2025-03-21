def find_permutations(test_cases):
    results = []
    
    for n, a in test_cases:
        freq = [0] * (n + 1)
        for num in a:
            freq[num] += 1
        
        # To keep track of the maximum valid prefix length for p1
        valid_prefix_length = 0
        valid_suffix_length = 0
        ways = []
        
        for i in range(1, n + 1):
            if freq[i] > 1:
                break
            valid_prefix_length += 1
            freq[i] -= 1
            
            if valid_prefix_length == i:
                # If we can form a valid permutation of length i
                valid_suffix_length = n - valid_prefix_length
                if valid_suffix_length >= 1 and valid_suffix_length <= n:
                    ways.append((valid_prefix_length, valid_suffix_length))
        
        # Reset freq for suffix checking
        freq = [0] * (n + 1)
        for num in reversed(a):
            freq[num] += 1
            
        for i in range(1, n + 1):
            if freq[i] > 1:
                break
            valid_suffix_length += 1
            freq[i] -= 1
            
            if valid_suffix_length == i:
                # If we can form a valid permutation of length i
                valid_prefix_length = n - valid_suffix_length
                if valid_prefix_length >= 1 and valid_prefix_length <= n:
                    ways.append((valid_prefix_length, valid_suffix_length))
        
        # Deduplicate symmetric cases
        unique_ways = set(ways)
        results.append((len(unique_ways), sorted(unique_ways)))
    
    return results

# Input reading and output formatting
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, a))
    index += 2

results = find_permutations(test_cases)

output = []
for count, pairs in results:
    output.append(str(count))
    for l1, l2 in pairs:
        output.append(f"{l1} {l2}")

print("\n".join(output))