def solve(n, k):
    # Minimum sum of the first k natural numbers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Initialize the array with the minimum valid values
    a = list(range(1, k + 1))
    current_sum = min_sum

    # Try to adjust the last element to reach n
    for i in range(k - 1, -1, -1):
        # Calculate the maximum value we can assign to a[i]
        max_value = 2 * a[i] if i < k - 1 else n - current_sum + a[i]
        # Ensure we don't exceed the required total n
        if current_sum < n:
            increment = min(max_value - a[i], n - current_sum)
            a[i] += increment
            current_sum += increment

        # If we have reached the required sum, we can stop
        if current_sum == n:
            break

    # Check if the conditions are satisfied
    valid = True
    for i in range(1, k):
        if not (a[i - 1] < a[i] <= 2 * a[i - 1]):
            valid = False
            break

    if valid and current_sum == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve(n, k)