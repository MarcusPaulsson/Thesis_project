def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Determine the positions of each character
    positions = defaultdict(list)
    for i, char in enumerate(s):
        positions[char].append(i)

    # Step 2: Create a color array
    color = [0] * n
    current_color = 1

    # Step 3: Assign colors based on the positions
    last_position = -1
    for char in sorted(positions.keys()):
        for pos in positions[char]:
            if last_position == -1 or pos > last_position:
                color[pos] = current_color
                last_position = pos
            else:
                # If we encounter a position that is not greater, we need a new color
                current_color += 1
                color[pos] = current_color
                last_position = pos

    # Step 4: Output the result
    print(current_color)
    print(' '.join(map(str, color)))

# Example usage:
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)