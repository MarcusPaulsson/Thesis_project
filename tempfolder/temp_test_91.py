def construct_permutation(t, test_cases):
    results = []
    for n, q in test_cases:
        p = [0] * n
        used = set()
        possible = True
        
        for i in range(n):
            if q[i] > (i + 1):
                possible = False
                break
            if i == 0 or q[i] > q[i - 1]:
                p[i] = q[i]  # Set p[i] to the new max
                used.add(q[i])
            else:
                # Find the smallest unused number that is less than q[i]
                for num in range(1, n + 1):
                    if num not in used:
                        p[i] = num
                        used.add(num)
                        break
        
        if possible and len(set(p)) == n:
            results.append(" ".join(map(str, p)))
        else:
            results.append("-1")
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    q = list(map(int, data[index + 1].split()))
    test_cases.append((n, q))
    index += 2

# Get results
results = construct_permutation(t, test_cases)

# Output results
print("\n".join(results))