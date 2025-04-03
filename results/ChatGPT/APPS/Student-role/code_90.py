def minimize_k(test_cases):
    results = []
    
    for n, a, l in test_cases:
        unlocked_values = [a[i] for i in range(n) if l[i] == 0]
        unlocked_values.sort()  # Sort unlocked values in ascending order
        index = 0
        
        new_a = []
        for i in range(n):
            if l[i] == 1:
                new_a.append(a[i])  # Keep locked values as is
            else:
                new_a.append(unlocked_values[index])  # Place sorted unlocked values
                index += 1
        
        results.append(new_a)
    
    return results

# Read input and process each test case
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    test_cases.append((n, a, l))

# Get the result for each test case
results = minimize_k(test_cases)

# Print the results
for result in results:
    print(' '.join(map(str, result)))