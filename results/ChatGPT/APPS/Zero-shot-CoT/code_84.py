n = int(input().strip())
s = input().strip()

sorted_s = sorted(s)
coloring = ['0'] * n

# Build a mapping of character to their positions in the sorted string
char_positions = {}
for idx, char in enumerate(sorted_s):
    if char not in char_positions:
        char_positions[char] = []
    char_positions[char].append(idx)

# To keep track of how many of each character we have colored
colored_count = {char: 0 for char in char_positions}

for i in range(n):
    char = s[i]
    # Get the actual position in the sorted array that this character would go to
    pos = char_positions[char][colored_count[char]]
    colored_count[char] += 1

    # If the color for current character is not set, set it to '0' or '1' depending on its position
    if coloring[pos] == '0':
        coloring[pos] = '0'
    else:
        coloring[pos] = '1'

# Check if the coloring can lead to a sorted arrangement
for i in range(1, n):
    if s[i] < s[i - 1] and coloring[i] == coloring[i - 1]:
        print("NO")
        break
else:
    print("YES")
    print(''.join(coloring))