def reconstruct_string(t, test_cases):
    results = []

    for s, x in test_cases:
        n = len(s)
        w = ['0'] * n

        for i in range(n):
            if s[i] == '1':
                if i - x >= 0:
                    w[i - x] = '1'
                if i + x < n:
                    w[i + x] = '1'

        valid = True
        for i in range(n):
            if s[i] == '1':
                if (i - x >= 0 and w[i - x] == '0') and (i + x < n and w[i + x] == '0'):
                    valid = False
                    break

        if valid:
            results.append(''.join(w))
        else:
            results.append('-1')

    return results


# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    s = input().strip()
    x = int(input().strip())
    test_cases.append((s, x))

# Processing and outputting results
results = reconstruct_string(t, test_cases)
for result in results:
    print(result)