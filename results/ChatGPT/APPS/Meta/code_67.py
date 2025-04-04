def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        if remaining_sum % 2 == 0:
            half_remaining_sum = remaining_sum // 2
            if half_remaining_sum in a[:i] + a[i+1:]:
                nice_indices.append(i + 1)  # store 1-based index

    print(len(nice_indices))
    if nice_indices:
        print(' '.join(map(str, nice_indices)))

# Input reading
n = int(input())
a = list(map(int, input().split()))

find_nice_indices(n, a)