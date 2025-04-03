def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Create a list to store the color for each character
    colors = [0] * n
    # Dictionary to store the last index of each character
    last_index = defaultdict(list)

    # Store the indices of each character in the string
    for i, char in enumerate(s):
        last_index[char].append(i)

    # To determine the minimum colors needed
    color = 1
    for char in sorted(last_index.keys()):
        indices = last_index[char]
        for idx in indices:
            if colors[idx] == 0:  # If not colored yet
                colors[idx] = color
        color += 1

    # Now we need to set the colors in such a way
    # that adjacent different colors can be swapped
    max_color = 0
    for i in range(n):
        if i > 0 and s[i] != s[i - 1]:
            # If we encounter different characters, we need to assign a new color
            max_color = max(max_color, colors[i - 1])
            colors[i] = max_color + 1
        else:
            # If the same character appears, keep the same color
            colors[i] = colors[i - 1]

    # The number of unique colors used
    unique_colors = len(set(colors))

    # Print the results
    print(unique_colors)
    print(' '.join(map(str, colors)))

# Example usage:
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)