def minimum_skip_points(test_cases):
    results = []
    for n, bosses in test_cases:
        skip_points = 0
        i = 0
        while i < n:
            if bosses[i] == 1:
                skip_points += 1
                if i + 1 < n and bosses[i + 1] == 1:
                    i += 2  # If there's another hard boss, skip it as well
                else:
                    i += 1  # Move to the next boss
            else:
                if i + 1 < n and bosses[i + 1] == 1:
                    i += 2  # You can take two easy bosses to skip the hard one
                else:
                    i += 1  # Just take the easy boss
        results.append(skip_points)
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    bosses = list(map(int, input().split()))
    test_cases.append((n, bosses))

# Getting results
results = minimum_skip_points(test_cases)

# Printing results
for result in results:
    print(result)