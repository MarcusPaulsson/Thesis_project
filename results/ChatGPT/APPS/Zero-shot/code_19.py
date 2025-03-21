def min_subscriptions(t, test_cases):
    results = []
    for n, k, d, shows in test_cases:
        min_subs = float('inf')
        show_count = {}
        left = 0
        
        for right in range(n):
            show_count[shows[right]] = show_count.get(shows[right], 0) + 1
            
            if right - left + 1 > d:
                show_count[shows[left]] -= 1
                if show_count[shows[left]] == 0:
                    del show_count[shows[left]]
                left += 1
            
            if right - left + 1 == d:
                min_subs = min(min_subs, len(show_count))

        results.append(min_subs)

    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n, k, d = map(int, data[index].split())
    shows = list(map(int, data[index + 1].split()))
    test_cases.append((n, k, d, shows))
    index += 2

# Get results and print
results = min_subscriptions(t, test_cases)
print("\n".join(map(str, results)))