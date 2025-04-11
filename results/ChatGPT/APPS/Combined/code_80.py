def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Identify the unique characters and their positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Step 2: Create a color mapping based on the positions of characters
    color = [0] * n
    color_count = 0

    # Step 3: Assign colors based on the positions of characters
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        for i in range(len(positions)):
            if i == 0:
                color[positions[i]] = color_count + 1
            else:
                # If the current character position is adjacent to the previous one, assign the same color
                if positions[i] - positions[i - 1] == 1:
                    color[positions[i]] = color[positions[i - 1]]
                else:
                    color_count += 1
                    color[positions[i]] = color_count + 1
        color_count += 1

    # Step 4: Output the results
    print(color_count)
    print(' '.join(map(str, color)))

# Example usage
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)