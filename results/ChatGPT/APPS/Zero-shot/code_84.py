def can_color_string(n, s):
    # Count the frequency of each character
    from collections import Counter
    freq = Counter(s)
    
    # Check if any character appears more than twice
    for count in freq.values():
        if count > 2:
            print("NO")
            return
    
    # Create a coloring array
    color = ['0'] * n
    # Assign colors based on the position of characters
    for i in range(n):
        if s[i] in freq:
            if freq[s[i]] > 0:
                color[i] = '0'
                freq[s[i]] -= 1
            else:
                color[i] = '1'
    
    print("YES")
    print(''.join(color))

# Read input
n = int(input().strip())
s = input().strip()
can_color_string(n, s)