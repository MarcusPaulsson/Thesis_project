def can_transform(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]

        can_increase = False
        can_decrease = False
        possible = True

        for j in range(n):
            if a[j] == 1:
                can_increase = True
            elif a[j] == -1:
                can_decrease = True

            if b[j] > a[j] and not can_increase:
                possible = False
                break
            elif b[j] < a[j] and not can_decrease:
                possible = False
                break

        results.append("YES" if possible else "NO")

    return results


# Input processing
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n = int(data[line_index])
    a = list(map(int, data[line_index + 1].split()))
    b = list(map(int, data[line_index + 2].split()))
    test_cases.append((n, a, b))
    line_index += 3

# Get the result and print
output = can_transform(t, test_cases)
print("\n".join(output))