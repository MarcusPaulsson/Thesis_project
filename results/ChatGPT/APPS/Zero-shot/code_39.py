def min_crossroad(test_cases):
    results = []
    
    for a, b, p, s in test_cases:
        n = len(s)
        total_cost = 0
        last_type = None
        
        for i in range(n - 1):
            if s[i] != last_type:
                if s[i] == 'A':
                    total_cost += a
                else:
                    total_cost += b
                last_type = s[i]
            
            if total_cost > p:
                results.append(i + 1)  # i is 0-based, we need 1-based
                break
        else:
            results.append(n)  # If we never broke, Petya can start at n (last crossroad)

    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    a, b, p = map(int, input().split())
    s = input().strip()
    test_cases.append((a, b, p, s))

# Getting results
results = min_crossroad(test_cases)

# Printing output
for result in results:
    print(result)