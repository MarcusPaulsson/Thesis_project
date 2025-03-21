def find_min_k(test_cases):
    results = []
    for case in test_cases:
        n, S = case
        S_set = set(S)
        possible_k = -1
        
        for k in range(1, 1024):
            transformed_set = {s ^ k for s in S}
            if transformed_set == S_set:
                possible_k = k
                break
        
        results.append(possible_k)
    
    return results


# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    test_cases.append((n, S))

# Finding results
results = find_min_k(test_cases)

# Printing results
for result in results:
    print(result)