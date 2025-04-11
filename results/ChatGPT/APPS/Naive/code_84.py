def can_color_string(n, s):
    # Create a list to store the color assignments
    color = ['0'] * n
    
    # Create a dictionary to count occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check for characters that appear more than twice
    for count in char_count.values():
        if count > 2:
            print("NO")
            return

    # Assign colors
    current_color = '0'
    for i in range(n):
        if s[i] in char_count and char_count[s[i]] > 0:
            color[i] = current_color
            char_count[s[i]] -= 1
            # Switch color if we have used both colors for this character
            if char_count[s[i]] == 0:
                current_color = '1' if current_color == '0' else '0'

    print("YES")
    print(''.join(color))

# Read input
n = int(input())
s = input().strip()
can_color_string(n, s)