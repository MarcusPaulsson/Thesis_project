def reconstruct_string(t, test_cases):
    results = []
    for case in test_cases:
        s, x = case
        n = len(s)
        # Initialize w with all '0's
        w = ['0'] * n
        
        for i in range(n):
            if s[i] == '1':
                if i - x >= 0:
                    w[i - x] = '1'
                if i + x < n:
                    w[i + x] = '1'
        
        # Validate if w can produce s
        valid = True
        for i in range(n):
            if s[i] == '1':
                if not ((i - x >= 0 and w[i - x] == '1') or (i + x < n and w[i + x] == '1')):
                    valid = False
                    break
            else:
                if (i - x >= 0 and w[i - x] == '1') or (i + x < n and w[i + x] == '1'):
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

# Get results and print
results = reconstruct_string(t, test_cases)
print("\n".join(results))