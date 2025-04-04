def can_color_to_sort(n, s):
    color = ['0'] * n
    last_seen = {}

    for i in range(n):
        char = s[i]
        if char in last_seen:
            if last_seen[char] == '0':
                color[i] = '1'
            else:
                color[i] = '0'
        else:
            last_seen[char] = color[i]

    # Check if the colored string can be sorted
    colored_pairs = [(s[i], color[i]) for i in range(n)]
    colored_pairs.sort()

    for i in range(1, n):
        if colored_pairs[i][0] == colored_pairs[i - 1][0] and colored_pairs[i][1] != colored_pairs[i - 1][1]:
            print("NO")
            return

    print("YES")
    print(''.join(color))

# Reading input
n = int(input().strip())
s = input().strip()
can_color_to_sort(n, s)