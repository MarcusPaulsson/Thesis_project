def process_test_cases(t, test_cases):
    results = []
    for n, a in test_cases:
        count_0 = a.count(0)
        count_1 = a.count(1)

        if count_0 > count_1:
            # Keep the majority of 0s or just enough 1s
            required = count_0
            if required % 2 != 0:
                required -= 1
            results.append(f"{required}")
            results.append("0 " * required)
        else:
            # Keep the majority of 1s or just enough 0s
            required = count_1
            if required % 2 != 0:
                required -= 1
            results.append(f"{required}")
            results.append("1 " * required)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process test cases
results = process_test_cases(t, test_cases)

# Print results
print("\n".join(results))