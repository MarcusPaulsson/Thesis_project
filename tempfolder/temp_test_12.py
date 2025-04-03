def can_transform(t, test_cases):
    results = []
    for _ in range(t):
        n = test_cases[_][0]
        a = test_cases[_][1]
        b = test_cases[_][2]

        can_increase = can_decrease = False

        for i in range(n):
            if a[i] == 1:
                can_increase = True
            elif a[i] == -1:
                can_decrease = True

            if can_increase and can_decrease:
                break

        possible = True
        for i in range(n):
            if b[i] > a[i] and not can_increase:
                possible = False
                break
            elif b[i] < a[i] and not can_decrease:
                possible = False
                break

        results.append("YES" if possible else "NO")
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    b = list(map(int, data[index + 2].split()))
    test_cases.append((n, a, b))
    index += 3

# Getting results
results = can_transform(t, test_cases)

# Printing results
print("\n".join(results))