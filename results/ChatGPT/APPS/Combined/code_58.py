def color_array(n, k, a):
    from collections import defaultdict

    color_assignment = [0] * n  # To store the color of each element
    color_count = defaultdict(int)  # To count occurrences of each color
    element_to_colors = defaultdict(set)  # To store which colors are assigned to each element

    # Step 2: Assign colors
    for i in range(n):
        element = a[i]
        # Try to assign a color to this element
        for color in range(1, k + 1):
            if color_count[color] < 1 and color not in element_to_colors[element]:
                color_assignment[i] = color
                color_count[color] += 1
                element_to_colors[element].add(color)
                break

    # Step 3: Check if we have assigned all colors
    if len(color_count) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color_assignment)))

# Example usage
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)