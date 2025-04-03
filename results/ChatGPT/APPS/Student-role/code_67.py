def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        if remaining_sum == 2 * a[i]:  # Check if the removed element is equal to the sum of the remaining elements
            nice_indices.append(i + 1)  # Store 1-based index

    print(len(nice_indices))
    if nice_indices:
        print(" ".join(map(str, nice_indices)))

# Input reading
n = int(input())
a = list(map(int, input().split()))

find_nice_indices(n, a)