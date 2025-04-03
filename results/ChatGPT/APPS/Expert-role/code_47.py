def max_strength(t, test_cases):
    results = []
    for n, a in test_cases:
        max_strength_value = 0
        # Sort the array based on the index of the original array
        sorted_a = sorted(a)
        # Calculate the maximum strength using the alternating sum
        for i in range(n):
            if i % 2 == 0:
                max_strength_value += sorted_a[i]
            else:
                max_strength_value -= sorted_a[i]
        results.append(max_strength_value)
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get the results and print them
results = max_strength(t, test_cases)
for result in results:
    print(result)