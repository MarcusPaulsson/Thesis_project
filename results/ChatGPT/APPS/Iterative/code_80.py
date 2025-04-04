def min_colors_to_sort(n, s):
    # To store the index of characters
    char_indices = {}

    # Collect the positions of each character
    for i, char in enumerate(s):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(i)

    # Initialize the colors array
    colors = [0] * n
    color = 0

    # Iterate through the sorted unique characters
    for char in sorted(char_indices.keys()):
        color += 1  # Increment the color for each unique character
        for idx in char_indices[char]:
            colors[idx] = color

    # The number of colors used is the maximum color value
    res = color

    print(res)
    print(' '.join(map(str, colors)))

# Read input
if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    min_colors_to_sort(n, s)