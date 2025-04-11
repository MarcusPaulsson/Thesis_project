def min_D_to_equalize(n, a):
    min_a = min(a)
    max_a = max(a)

    if max_a == min_a:
        return 0

    # Calculate the possible D values
    possible_D = (max_a - min_a) // 2

    # Check if we can achieve equality with this D
    if (max_a - min_a) % 2 == 0:
        return possible_D
    else:
        return -1

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_D_to_equalize(n, a))