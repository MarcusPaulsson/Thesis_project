def polycarp_training(n, k):
    # Calculate the minimum sum of problems required with the given constraints
    min_sum = k * (k + 1) // 2  # Minimum problems if we solve 1, 2, ..., k problems
    if n < min_sum:
        print("NO")
        return

    # Start with the minimum valid array
    a = list(range(1, k + 1))
    current_sum = min_sum

    # Distribute the remaining problems
    remaining = n - current_sum

    for i in range(k - 1, -1, -1):
        # Max we can add to a[i] is 2 * a[i] - a[i] = a[i] (to satisfy a[i] < a[i+1] <= 2 * a[i])
        max_increase = a[i]  # We can at most double the previous day's count
        if remaining > 0:
            increase = min(max_increase, remaining)
            a[i] += increase
            remaining -= increase

    if remaining > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage
n, k = map(int, input().split())
polycarp_training(n, k)