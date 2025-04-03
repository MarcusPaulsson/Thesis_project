def distribute_gifts(t, test_cases):
    result = []
    
    for case in test_cases:
        n, a, b = case
        a.sort()
        b.sort(reverse=True)
        
        result.append(' '.join(map(str, a)))
        result.append(' '.join(map(str, b)))
    
    return '\n'.join(result)

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Get the results and print them
output = distribute_gifts(t, test_cases)
print(output)