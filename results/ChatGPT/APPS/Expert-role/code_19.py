def check_records(test_cases):
    results = []
    for case in test_cases:
        n, stats = case
        valid = True
        for i in range(1, n):
            p_prev, c_prev = stats[i - 1]
            p_curr, c_curr = stats[i]
            if p_curr < p_prev or c_curr < c_prev or c_curr > p_curr:
                valid = False
                break
            if (p_curr - p_prev) < (c_curr - c_prev):
                valid = False
                break
        results.append("YES" if valid else "NO")
    return results

# Input reading and output printing
import sys

input = sys.stdin.read
data = input().splitlines()
index = 0
T = int(data[index])
index += 1
test_cases = []

for _ in range(T):
    n = int(data[index])
    index += 1
    stats = []
    for __ in range(n):
        p, c = map(int, data[index].split())
        stats.append((p, c))
        index += 1
    test_cases.append((n, stats))

results = check_records(test_cases)
for result in results:
    print(result)