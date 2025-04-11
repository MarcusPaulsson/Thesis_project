def can_color_string(n, s):
    # Count the occurrences of each character
    from collections import Counter
    count = Counter(s)

    # Check if any character appears more than twice
    for char, cnt in count.items():
        if cnt > 2:
            print("NO")
            return

    # Create a coloring array
    color = ['0'] * n

    # Assign colors based on the character positions
    for i in range(n):
        if s[i] == s[i - 1] if i > 0 else None:
            color[i] = color[i - 1]
        else:
            color[i] = '1' if color[i - 1] == '0' else '0'

    print("YES")
    print(''.join(color))

# Input reading
n = int(input().strip())
s = input().strip()

can_color_string(n, s)