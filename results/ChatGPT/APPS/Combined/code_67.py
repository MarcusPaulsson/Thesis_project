def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        # Calculate the remaining sum after removing a[i]
        remaining_sum = total_sum - a[i]
        # Check if the remaining sum is even and if half of it exists in the array
        if remaining_sum % 2 == 0 and (remaining_sum // 2) in a:
            # Ensure that we are not counting the removed element itself
            if (remaining_sum // 2) != a[i] or a.count(a[i]) > 1:
                nice_indices.append(i + 1)

    return nice_indices

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    nice_indices = find_nice_indices(n, a)
    
    print(len(nice_indices))
    if nice_indices:
        print(" ".join(map(str, nice_indices)))