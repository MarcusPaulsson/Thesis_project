def solve_problems(n, k):
    # Minimum sum of problems required: 1 + 2 + 3 + ... + k = k * (k + 1) // 2
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        print("NO")
        return

    # Maximum sum of problems we can reach: 1 * 2^(k-1) + 2^(k-1) + 2^(k-2) + ... + 2^0
    # This is a geometric series with the first term as 1 and ratio as 2.
    max_sum = (1 << k) - 1  # 2^k - 1
    if n > max_sum:
        print("NO")
        return

    # Now, we need to construct the sequence
    a = [0] * k
    # Start with the minimum valid sequence
    for i in range(k):
        a[i] = i + 1

    current_sum = min_sum
    for i in range(k - 1, -1, -1):
        # While current_sum is less than n, try to increase a[i]
        while current_sum < n:
            if a[i] * 2 <= (a[i + 1] if i + 1 < k else float('inf')):  # can double
                current_sum += a[i]
                a[i] *= 2
            else:
                break

    if current_sum == n:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")

# Read input
n, k = map(int, input().split())
solve_problems(n, k)