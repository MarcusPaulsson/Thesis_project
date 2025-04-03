def find_permutation(t, test_cases):
    results = []
    for _ in range(t):
        n = test_cases[_][0]
        q = test_cases[_][1]
        
        used = set()
        p = []
        possible = True
        
        for i in range(n):
            if q[i] > (i + 1):  # Check if q[i] is greater than the current index + 1
                possible = False
                break
            
            if i == 0 or q[i] != q[i - 1]:
                p.append(q[i])
                used.add(q[i])
            else:
                # We need to find the smallest unused number
                for num in range(1, n + 1):
                    if num not in used:
                        p.append(num)
                        used.add(num)
                        break
        
        if possible:
            results.append(" ".join(map(str, p)))
        else:
            results.append("-1")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    test_cases.append((n, q))

# Get results
results = find_permutation(t, test_cases)

# Print results
for result in results:
    print(result)