def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)

    if min_a == max_a:
        return 0  # All elements are already equal

    # Calculate the difference between the maximum and minimum values
    diff = max_a - min_a

    # Check if the difference can be evenly divided into three parts
    if diff % 2 == 0:
        return diff // 2
    else:
        return -1

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(find_minimum_D(n, a))