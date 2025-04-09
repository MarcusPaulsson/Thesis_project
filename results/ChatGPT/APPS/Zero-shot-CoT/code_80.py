def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Create a mapping of character index positions
    positions = defaultdict(list)
    for index, char in enumerate(s):
        positions[char].append(index)

    # Step 2: Initialize the colors array
    colors = [0] * n
    current_color = 1
    
    # Step 3: Assign colors based on character positions
    for char in sorted(positions.keys()):
        for pos in positions[char]:
            colors[pos] = current_color
        current_color += 1

    # The maximum color used is the number of colors needed
    max_colors = max(colors)

    # Output the results
    print(max_colors)
    print(" ".join(map(str, colors)))


# Input reading
n = int(input().strip())
s = input().strip()

# Call the function
min_colors_to_sort(n, s)