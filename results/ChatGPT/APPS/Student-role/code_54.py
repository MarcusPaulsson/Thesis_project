def min_D_to_equal_elements(n, a):
    min_a = min(a)
    max_a = max(a)

    if max_a == min_a:
        return 0  # All elements are already equal

    # Calculate the possible D
    possible_D = (max_a - min_a) // 2

    # Check if it is possible to make all elements equal
    target1 = min_a + possible_D
    target2 = max_a - possible_D

    if target1 == target2:
        return possible_D
    else:
        return -1

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
result = min_D_to_equal_elements(n, a)
print(result)