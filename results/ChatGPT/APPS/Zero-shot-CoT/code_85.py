def reconstruct_string(t, test_cases):
    results = []
    
    for s, x in test_cases:
        n = len(s)
        w = ['0'] * n
        
        # Mark positions in w based on s
        for i in range(n):
            if s[i] == '1':
                if i - x >= 0:
                    w[i - x] = '1'
                if i + x < n:
                    w[i + x] = '1'
        
        # Validate the constructed w against s
        valid = True
        for i in range(n):
            if s[i] == '1':
                if not (i - x >= 0 and w[i - x] == '1') and not (i + x < n and w[i + x] == '1'):
                    valid = False
                    break
        
        if valid:
            results.append(''.join(w))
        else:
            results.append('-1')
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    s = input().strip()
    x = int(input().strip())
    test_cases.append((s, x))

# Process the test cases
results = reconstruct_string(t, test_cases)

# Output results
for result in results:
    print(result)