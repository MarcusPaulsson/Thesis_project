def min_max_lis_sequences(t, test_cases):
    results = []
    for n, s in test_cases:
        # Minimum LIS sequence
        min_seq = [0] * n
        # Fill increasing parts
        i = 0
        while i < n:
            start = i
            while i + 1 < n and s[i] == '<':
                i += 1
            # Fill the increasing segment
            for j in range(start, i + 1):
                min_seq[j] = j - start + 1
            i += 1
        # Fill decreasing parts
        for i in range(n):
            if min_seq[i] == 0:
                min_seq[i] = n - (i - 1)
        
        # Maximum LIS sequence
        max_seq = [0] * n
        # Fill decreasing parts
        i = 0
        while i < n:
            start = i
            while i + 1 < n and s[i] == '>':
                i += 1
            # Fill the decreasing segment
            for j in range(start, i + 1):
                max_seq[j] = start + (i - start + 1 - (j - start))
            i += 1
        # Fill increasing parts
        for i in range(n):
            if max_seq[i] == 0:
                max_seq[i] = (n - (i - start))

        results.append((min_seq, max_seq))
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [(int(line.split()[0]), line.split()[1]) for line in data[1:t + 1]]

results = min_max_lis_sequences(t, test_cases)

# Print results
output = []
for min_seq, max_seq in results:
    output.append(" ".join(map(str, min_seq)))
    output.append(" ".join(map(str, max_seq)))

print("\n".join(output))