def min_max_lis(t, test_cases):
    results = []
    for n, s in test_cases:
        # Build the minimum LIS sequence
        min_seq = [0] * n
        left = 1
        right = n
        
        # Fill in the increasing parts
        i = 0
        while i < n - 1:
            if s[i] == '<':
                start = i
                while i < n - 1 and s[i] == '<':
                    i += 1
                for j in range(start, i + 1):
                    min_seq[j] = left
                    left += 1
            else:
                start = i
                while i < n - 1 and s[i] == '>':
                    i += 1
                for j in range(start, i + 1):
                    min_seq[j] = right
                    right -= 1
        
        # Reset for maximum LIS sequence
        max_seq = [0] * n
        left = 1
        right = n
        
        # Fill in the decreasing parts
        i = 0
        while i < n - 1:
            if s[i] == '>':
                start = i
                while i < n - 1 and s[i] == '>':
                    i += 1
                for j in range(start, i + 1):
                    max_seq[j] = right
                    right -= 1
            else:
                start = i
                while i < n - 1 and s[i] == '<':
                    i += 1
                for j in range(start, i + 1):
                    max_seq[j] = left
                    left += 1

        results.append((min_seq, max_seq))

    return results


# Input reading
import sys
input = sys.stdin.read

data = input().splitlines()
t = int(data[0])
test_cases = []
for i in range(1, t + 1):
    n, s = data[i].split()
    test_cases.append((int(n), s))

# Processing
results = min_max_lis(t, test_cases)

# Output
output = []
for min_seq, max_seq in results:
    output.append(' '.join(map(str, min_seq)))
    output.append(' '.join(map(str, max_seq)))

print('\n'.join(output))