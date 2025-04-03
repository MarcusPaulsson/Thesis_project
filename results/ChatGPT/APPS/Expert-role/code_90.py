def rearrange_array(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        l = test_cases[i][2]

        unlocked_values = [a[j] for j in range(n) if l[j] == 0]
        unlocked_values.sort()

        result = []
        unlocked_index = 0
        for j in range(n):
            if l[j] == 1:
                result.append(a[j])
            else:
                result.append(unlocked_values[unlocked_index])
                unlocked_index += 1

        results.append(result)

    return results


# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    test_cases.append((n, a, l))

# Get the rearranged arrays
results = rearrange_array(t, test_cases)

# Output the results
for result in results:
    print(' '.join(map(str, result)))