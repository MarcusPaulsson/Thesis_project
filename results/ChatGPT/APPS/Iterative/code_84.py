def can_be_sorted(n, s):
    last_position = {}
    color = ['0'] * n

    for i in range(n):
        if s[i] in last_position:
            if last_position[s[i]] + 1 < i:
                # Alternate colors for characters that have appeared before and are not adjacent
                color[i] = '1' if color[last_position[s[i]]] == '0' else '0'
        last_position[s[i]] = i

    # Check if there are any adjacent characters that are out of order and have the same color
    for i in range(n - 1):
        if s[i] > s[i + 1] and color[i] == color[i + 1]:
            print("NO")
            return

    print("YES")
    print(''.join(color))


n = int(input())
s = input().strip()
can_be_sorted(n, s)