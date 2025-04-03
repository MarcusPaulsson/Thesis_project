def minimize_misfortune(t, test_cases):
    results = []
    for n, T, a in test_cases:
        color = [0] * n
        freq = {}
        
        for i in range(n):
            if a[i] in freq:
                freq[a[i]].append(i)
            else:
                freq[a[i]] = [i]

        for num in freq:
            complement = T - num
            if num == complement:
                # If num and complement are the same, we can paint half and half
                indices = freq[num]
                for i in range(len(indices)):
                    color[indices[i]] = i % 2
            elif complement in freq:
                # Paint all `num` in one color and `complement` in the other
                for index in freq[num]:
                    color[index] = 0
                for index in freq[complement]:
                    color[index] = 1

        results.append(color)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, T, a))

# Get results
results = minimize_misfortune(t, test_cases)

# Output results
for result in results:
    print(" ".join(map(str, result)))