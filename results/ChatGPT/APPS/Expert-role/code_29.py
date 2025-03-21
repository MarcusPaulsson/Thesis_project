def k_amazing_numbers(t, test_cases):
    results = []
    for n, a in test_cases:
        last_position = {}
        min_in_all_segments = [-1] * n
        
        # Store last position of each number
        for i in range(n):
            last_position[a[i]] = i
        
        # Check for each k from 1 to n
        for k in range(1, n + 1):
            # Dictionary to count occurrences in the last k segments
            count = {}
            valid_numbers = set()
            for i in range(n):
                if i >= k:
                    # Remove the contribution of a[i - k]
                    count[a[i - k]] -= 1
                    if count[a[i - k]] == 0:
                        del count[a[i - k]]
                
                # Add the current number
                count[a[i]] = count.get(a[i], 0) + 1
                
                if i >= k - 1:
                    # Check if we have the number in the last k segment
                    if count[a[i]] == 1 and a[i] not in valid_numbers:
                        valid_numbers.add(a[i])
                    if len(valid_numbers) == 0:
                        min_in_all_segments[k - 1] = -1
                    else:
                        min_in_all_segments[k - 1] = min(valid_numbers)
        
        results.append(" ".join(map(str, min_in_all_segments)))

    return results


# Reading input and outputting results
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

results = k_amazing_numbers(t, test_cases)
print("\n".join(results))