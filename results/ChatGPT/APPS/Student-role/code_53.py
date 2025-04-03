def min_max_lis(t, test_cases):
    results = []
    
    for n, s in test_cases:
        # Constructing sequence for minimum LIS
        min_seq = []
        left = 1
        right = n
        
        for char in s:
            if char == '<':
                min_seq.append(left)
                left += 1
            else:
                min_seq.append(right)
                right -= 1
        
        min_seq.append(left)  # Append the last remaining number
        results.append(" ".join(map(str, min_seq)))
        
        # Constructing sequence for maximum LIS
        max_seq = []
        left = 1
        right = n
        
        for char in s:
            if char == '<':
                max_seq.append(left)
                left += 1
            else:
                max_seq.append(right)
                right -= 1
        
        max_seq.append(left)  # Append the last remaining number
        results.append(" ".join(map(str, max_seq[::-1])))  # Reverse for max LIS
        
    return results

# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = [(int(line.split()[0]), line.split()[1]) for line in data[1:t+1]]

# Get results
results = min_max_lis(t, test_cases)

# Output results
print("\n".join(results))