def color_array(n, k, a):
    from collections import defaultdict

    # Dictionary to keep track of color usage
    color_map = defaultdict(list)

    # Fill color_map with indices of each element in array a
    for index, value in enumerate(a):
        color_map[value].append(index)

    # Check if any value in color_map has more than k occurrences
    if any(len(indices) > k for indices in color_map.values()):
        print("NO")
        return

    # Prepare a color assignment array
    colors = [0] * n
    current_color = 1

    # Assign colors
    for indices in color_map.values():
        for index in indices:
            colors[index] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    # Check if all colors from 1 to k are used
    used_colors = set(colors)
    if len(used_colors) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, colors)))

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function
color_array(n, k, a)