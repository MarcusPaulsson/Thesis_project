def find_sequences(t, cases):
    results = []
    for n, s in cases:
        # Calculate the minimum LIS sequence
        min_seq = []
        max_seq = []
        
        # Create the minimum LIS sequence
        # Fill in increasing segments for '<' and decreasing segments for '>'
        current_num = 1
        i = 0
        
        while i < n - 1:
            if s[i] == '<':
                start = i
                while i < n - 1 and s[i] == '<':
                    i += 1
                # Fill the increasing segment
                for j in range(start, i + 1):
                    min_seq.append(current_num)
                    current_num += 1
            else:
                start = i
                while i < n - 1 and s[i] == '>':
                    i += 1
                # Fill the decreasing segment
                temp = []
                for j in range(start, i + 1):
                    temp.append(current_num)
                    current_num += 1
                min_seq.extend(reversed(temp))
        
        # Reset and create the maximum LIS sequence
        current_num = 1
        i = 0
        
        while i < n - 1:
            if s[i] == '>':
                start = i
                while i < n - 1 and s[i] == '>':
                    i += 1
                # Fill the decreasing segment
                for j in range(start, i + 1):
                    max_seq.append(current_num)
                    current_num += 1
            else:
                start = i
                while i < n - 1 and s[i] == '<':
                    i += 1
                # Fill the increasing segment
                temp = []
                for j in range(start, i + 1):
                    temp.append(current_num)
                    current_num += 1
                max_seq.extend(temp)
        
        results.append((min_seq, max_seq))
    
    return results


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
cases = []

for i in range(1, t + 1):
    n, s = data[i].split()
    cases.append((int(n), s))

# Get results
results = find_sequences(t, cases)

# Print results
output = []
for min_seq, max_seq in results:
    output.append(' '.join(map(str, min_seq)))
    output.append(' '.join(map(str, max_seq)))

print('\n'.join(output))