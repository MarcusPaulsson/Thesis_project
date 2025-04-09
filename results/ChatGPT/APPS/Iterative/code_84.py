def can_color_string(n, s):
    # Create a list to keep track of the frequency of each character
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
        
    # Check if any character occurs more than twice
    if any(count > 2 for count in freq):
        print("NO")
        return
    
    # Create the coloring based on the character positions
    color = ['0'] * n
    current_color = 0
    last_char = None
    
    for i in range(n):
        if last_char is None or s[i] != last_char:
            current_color = 1 - current_color  # Alternate colors
        color[i] = str(current_color)
        last_char = s[i]
    
    print("YES")
    print("".join(color))

# Read input
n = int(input())
s = input().strip()
can_color_string(n, s)