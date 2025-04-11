def color_array(n, k, a):
    from collections import defaultdict

    color_assignment = [0] * n
    color_count = defaultdict(int)
    element_positions = defaultdict(list)

    # Collect positions of each element
    for index, value in enumerate(a):
        element_positions[value].append(index)

    # Check if we can color the array
    if any(len(positions) > k for positions in element_positions.values()):
        print("NO")
        return

    # Assign colors
    current_color = 1
    for positions in element_positions.values():
        for pos in positions:
            color_assignment[pos] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    print("YES")
    print(" ".join(map(str, color_assignment)))

# Example usage:
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# color_array(n, k, a)