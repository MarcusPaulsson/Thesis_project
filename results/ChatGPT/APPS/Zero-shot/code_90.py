def rearrange_array(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a, l = case
        unlocked_values = [a[i] for i in range(n) if l[i] == 0]
        unlocked_values.sort()  # Sort unlocked values
        
        j = 0
        result = []
        
        for i in range(n):
            if l[i] == 1:
                result.append(a[i])  # Keep locked values
            else:
                result.append(unlocked_values[j])  # Replace with sorted unlocked values
                j += 1
        
        results.append(result)

    return results

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    test_cases.append((n, a, l))

# Getting results
results = rearrange_array(t, test_cases)

# Output results
for result in results:
    print(" ".join(map(str, result)))