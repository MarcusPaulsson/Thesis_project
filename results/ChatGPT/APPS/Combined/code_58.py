def color_array(n, k, a):
    from collections import defaultdict

    # Step 1: Initialize variables
    color_assignment = [0] * n
    frequency = defaultdict(list)

    # Step 2: Organize indices of each unique number
    for index, value in enumerate(a):
        frequency[value].append(index)

    # Step 3: Check if coloring is possible
    if len(frequency) > k:
        return "NO"

    # Step 4: Assign colors
    current_color = 1
    for indices in frequency.values():
        for i, index in enumerate(indices):
            color_assignment[index] = (i % k) + 1

    return "YES", color_assignment

# Example usage:
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# result = color_array(n, k, a)
# if result == "NO":
#     print(result)
# else:
#     print(result[0])
#     print(" ".join(map(str, result[1])))