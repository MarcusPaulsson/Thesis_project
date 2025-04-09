def can_construct_symmetric_square(t, test_cases):
    results = []

    for n, m, tiles in test_cases:
        if m % 2 != 0:
            results.append("NO")
            continue

        can_form_symmetric = False

        # Check for symmetric conditions
        for a, b, c, d in tiles:
            if b == c:  # Check if top-right matches bottom-left
                can_form_symmetric = True
                break

        results.append("YES" if can_form_symmetric else "NO")

    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    tiles = [tuple(map(int, input().split())) + tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, tiles))

# Process and print results
results = can_construct_symmetric_square(t, test_cases)
print("\n".join(results))