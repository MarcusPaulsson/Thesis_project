def has_palindromic_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        # Use a dictionary to track the first occurrence of each number
        first_occurrence = {}
        for i in range(n):
            if a[i] in first_occurrence:
                # If we find a number that has appeared before
                # and the distance between their indices is at least 2
                if i - first_occurrence[a[i]] >= 2:
                    found = True
                    break
            else:
                first_occurrence[a[i]] = i
        
        if found:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Getting results and printing
results = has_palindromic_subsequence(test_cases)
for result in results:
    print(result)