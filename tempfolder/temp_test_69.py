def min_cost_to_detonate(t, test_cases):
    results = []
    
    for case in test_cases:
        a, b, s = case
        n = len(s)
        
        # Find all segments of mines
        segments = s.split('0')
        segments = [seg for seg in segments if seg]  # Keep only non-empty segments
        
        if not segments:
            results.append(0)
            continue
        
        total_cost = 0
        
        # Activate the first segment
        total_cost += a
        
        # For each subsequent segment, we have two choices:
        # 1. Activate it (cost a)
        # 2. Place a mine in between (cost b) + activate it (cost a)
        
        for seg in segments[1:]:
            # If we place a mine and then activate, total cost is b + a
            # If we just activate, total cost is a
            total_cost += min(a, b + a)
        
        results.append(total_cost)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, 2 * t, 2):
    a, b = map(int, data[i].split())
    s = data[i + 1]
    test_cases.append((a, b, s))

# Get results
results = min_cost_to_detonate(t, test_cases)

# Print results
for result in results:
    print(result)