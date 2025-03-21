def min_subscriptions(t, test_cases):
    results = []
    
    for case in test_cases:
        n, k, d = case[0]
        a = case[1]
        
        min_subs = float('inf')
        count = {}
        
        for i in range(n):
            if i >= d:
                # Remove the element that is out of the window
                count[a[i - d]] -= 1
                if count[a[i - d]] == 0:
                    del count[a[i - d]]
            
            # Add the current element
            if a[i] in count:
                count[a[i]] += 1
            else:
                count[a[i]] = 1
            
            # When we have a valid window of size d, check the number of unique shows
            if i >= d - 1:
                min_subs = min(min_subs, len(count))
        
        results.append(min_subs)
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append(((n, k, d), a))

# Get results
results = min_subscriptions(t, test_cases)

# Output results
for result in results:
    print(result)