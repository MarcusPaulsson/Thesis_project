def has_palindrome_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        # Use a dictionary to track the first occurrence of each number
        first_occurrence = {}
        
        for i in range(n):
            if a[i] in first_occurrence:
                # If we find the same number again, we can form a palindrome
                if i - first_occurrence[a[i]] >= 2:
                    found = True
                    break
            else:
                first_occurrence[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = has_palindrome_subsequence(test_cases)
print("\n".join(results))