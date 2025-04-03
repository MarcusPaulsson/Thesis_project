def reconstruct_string(t, test_cases):
    results = []
    
    for s, x in test_cases:
        n = len(s)
        w = ['0'] * n
        
        # Step 1: Mark potential 1's in w based on s
        for i in range(n):
            if s[i] == '1':
                if i - x >= 0:
                    w[i - x] = '1'
                if i + x < n:
                    w[i + x] = '1'
        
        # Step 2: Verify if this w can produce s
        valid = True
        for i in range(n):
            s_generated = '0'
            if (i - x >= 0 and w[i - x] == '1') or (i + x < n and w[i + x] == '1'):
                s_generated = '1'
            if s_generated != s[i]:
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

# Get results and print them
results = reconstruct_string(t, test_cases)
for result in results:
    print(result)