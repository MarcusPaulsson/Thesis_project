def min_blows_to_defeat(t, queries):
    results = []
    for n, x in queries:
        blows = 0
        for d_i, h_i in sorted(zip(d, h), key=lambda p: p[0] - p[1], reverse=True):
            if x > 0:
                blows += (x + d_i - 1) // d_i
                x = max(0, x - d_i + h_i)
        if x == 0:
            results.append(blows)
        else:
            results.append(-1)
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
t = int(data[0])
queries = []
index = 1
for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    index += 2
    d = []
    h = []
    for _ in range(n):
        d_i = int(data[index])
        h_i = int(data[index + 1])
        d.append(d_i)
        h.append(h_i)
        index += 2

# Calculate results
results = min_blows_to_defeat(t, queries)

# Print output
for result in results:
    print(result)