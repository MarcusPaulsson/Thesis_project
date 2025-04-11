def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Create a list to store the color for each character
    colors = [0] * n
    # Dictionary to track the last position of each character
    last_position = defaultdict(list)

    # Fill the last_position with indices of each character
    for i, char in enumerate(s):
        last_position[char].append(i)

    # Initialize the color counter
    color_count = 0
    # A set to track the used colors
    used_colors = set()

    # Iterate through the string to assign colors
    for i in range(n):
        char = s[i]
        # If the character is already colored, continue
        if colors[i] != 0:
            continue
        
        # Assign a new color
        color_count += 1
        current_color = color_count
        colors[i] = current_color
        used_colors.add(current_color)

        # Check the last positions of the current character
        for pos in last_position[char]:
            if colors[pos] == 0:
                colors[pos] = current_color

        # Now we need to ensure that we can swap with different colors
        for j in range(i + 1, n):
            if s[j] < s[i] and colors[j] == 0:
                colors[j] = current_color

    # Output the results
    print(color_count)
    print(" ".join(map(str, colors)))

# Example usage:
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)