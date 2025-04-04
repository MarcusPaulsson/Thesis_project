def can_color_sort(n, s):
    color = ['0'] * n
    last_pos = {}
    
    for i in range(n):
        char = s[i]
        if char in last_pos:
            # If the same character appears again, we check the last position
            if last_pos[char] is not None:
                # Check if the character before the last occurrence is different
                if s[last_pos[char]] != char:
                    # Color it differently
                    color[i] = '1' if color[last_pos[char]] == '0' else '0'
                # Update last position
                last_pos[char] = i
            else:
                last_pos[char] = i
        else:
            last_pos[char] = i
    
    # Check for any conflicts while coloring
    for i in range(n - 1):
        if s[i] == s[i + 1] and color[i] != color[i + 1]:
            print("NO")
            return
    
    print("YES")
    print(''.join(color))

# Input reading
n = int(input())
s = input()

can_color_sort(n, s)