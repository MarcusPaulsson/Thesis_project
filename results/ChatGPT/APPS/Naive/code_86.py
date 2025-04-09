def solve_polycarp(n, k):
    # Minimum sum of problems solved in k days
    min_sum = k * (k + 1) // 2  # This is 1 + 2 + ... + k
    if n < min_sum:
        print("NO")
        return
    
    # Maximum sum of problems based on the doubling rule
    # If we start with 1, 2, ..., k, we can double it to get a maximum
    max_sum = k * (2 * k + 1) // 2  # This is 1 + 2 + ... + k, then double it
    if n > max_sum:
        print("NO")
        return
    
    # We can construct the solution
    a = list(range(1, k + 1))
    current_sum = sum(a)
    
    # We need to increase the sum to n
    delta = n - current_sum
    
    # We will try to increase the last element as much as we can
    for i in range(k - 1, -1, -1):
        max_increase = a[i]  # We can increase a[i] to at most 2 * a[i]
        increase = min(delta, max_increase)
        a[i] += increase
        delta -= increase
        if delta <= 0:
            break
    
    if delta > 0:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))

# Example usage:
solve_polycarp(26, 6)
solve_polycarp(8, 3)
solve_polycarp(1, 1)
solve_polycarp(9, 4)
solve_polycarp(7, 2)