def rearrange_array(test_cases):
    results = []
    
    for n, a, l in test_cases:
        unlocked_values = [a[i] for i in range(n) if l[i] == 0]
        unlocked_values.sort()  # Sort unlocked values to minimize negative prefix sums
        
        result = a[:]  # Copy original array
        j = 0  # Index for unlocked_values
        
        for i in range(n):
            if l[i] == 0:
                result[i] = unlocked_values[j]
                j += 1
        
        results.append(result)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    test_cases.append((n, a, l))

output = rearrange_array(test_cases)

# Print output
for result in output:
    print(' '.join(map(str, result)))