def min_crossroad(test_cases):
    results = []
    for a, b, p, s in test_cases:
        n = len(s)
        total_cost = 0
        last_type = ''
        
        # Traverse from the end to the start
        for i in range(n - 1, -1, -1):
            if s[i] != last_type:
                # We have encountered a new segment
                if s[i] == 'A':
                    total_cost += a
                else:
                    total_cost += b
                last_type = s[i]
            
            # Check if the total cost is within the money Petya has
            if total_cost <= p:
                results.append(i + 1)  # +1 for 1-based index
                break

    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    a, b, p = map(int, data[index].split())
    s = data[index + 1].strip()
    test_cases.append((a, b, p, s))
    index += 2

# Get results and print them
results = min_crossroad(test_cases)
for res in results:
    print(res)