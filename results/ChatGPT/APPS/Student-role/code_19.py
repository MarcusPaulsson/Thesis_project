def min_subscriptions(t, test_cases):
    results = []
    
    for case in test_cases:
        n, k, d, shows = case
        show_count = {}
        min_subs = float('inf')
        
        # Sliding window approach
        for i in range(n):
            if i >= d:
                # Remove the show that is sliding out of the window
                show_count[shows[i - d]] -= 1
                if show_count[shows[i - d]] == 0:
                    del show_count[shows[i - d]]
            
            # Add the current show in the window
            if shows[i] in show_count:
                show_count[shows[i]] += 1
            else:
                show_count[shows[i]] = 1
            
            # If we have processed at least 'd' days
            if i >= d - 1:
                min_subs = min(min_subs, len(show_count))
        
        results.append(min_subs)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, k, d = map(int, input().split())
    shows = list(map(int, input().split()))
    test_cases.append((n, k, d, shows))

# Get results
results = min_subscriptions(t, test_cases)

# Print results
for result in results:
    print(result)