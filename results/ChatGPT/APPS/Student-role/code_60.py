def has_palindrome_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        # Use a dictionary to track the first and last occurrence of each number
        positions = {}
        for i in range(n):
            if a[i] in positions:
                positions[a[i]].append(i)
            else:
                positions[a[i]] = [i]
        
        # Check for a palindrome subsequence of length at least 3
        for key, pos in positions.items():
            if len(pos) >= 2 and pos[-1] - pos[0] >= 2:
                found = True
                break
        
        results.append("YES" if found else "NO")
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = has_palindrome_subsequence(t, test_cases)
for result in results:
    print(result)