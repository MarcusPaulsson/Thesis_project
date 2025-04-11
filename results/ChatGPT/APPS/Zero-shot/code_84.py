def can_color_string(n, s):
    # Count frequency of each character
    from collections import Counter
    freq = Counter(s)
    
    # Check if any character appears more than twice
    for count in freq.values():
        if count > 2:
            print("NO")
            return
    
    # Create a coloring array
    color = ['0'] * n
    
    # Assign colors
    last_color = '0'
    for i in range(n):
        if s[i] in freq and freq[s[i]] > 0:
            if freq[s[i]] == 1:
                color[i] = last_color
            else:
                color[i] = '0' if last_color == '1' else '1'
            freq[s[i]] -= 1
            last_color = color[i]
    
    print("YES")
    print(''.join(color))

# Read input
n = int(input())
s = input().strip()
can_color_string(n, s)