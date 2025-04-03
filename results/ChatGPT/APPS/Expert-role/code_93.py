def minimum_time_to_send_presents(t, test_cases):
    results = []
    for case in test_cases:
        n, m, a, b = case
        position = {present: i for i, present in enumerate(a)}
        time = 0
        current_top = n  # Initially, all presents are below the top

        for present in b:
            index = position[present]
            k = current_top - index - 1  # Number of presents above the current present
            time += 2 * k + 1  # Time to send the present
            current_top = index  # Update the top position after taking the present

        results.append(time)

    return results

# Reading inputs
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

results = minimum_time_to_send_presents(t, test_cases)
for result in results:
    print(result)