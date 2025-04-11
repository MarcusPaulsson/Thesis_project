def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        if (total_sum - a[i]) % 2 == 0:
            target = (total_sum - a[i]) // 2
            if target in a:
                # Check if the target is not the same as a[i] or if it appears more than once
                if target != a[i] or a.count(target) > 1:
                    nice_indices.append(i + 1)  # Store 1-based index

    print(len(nice_indices))
    if nice_indices:
        print(" ".join(map(str, nice_indices)))

# Example usage
n = int(input())
a = list(map(int, input().split()))
find_nice_indices(n, a)