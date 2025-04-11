def can_color_string(n, s):
    from collections import Counter
    
    # Step 1: Count occurrences of each character
    count = Counter(s)
    
    # Step 2: Check if any character appears more than twice
    if any(cnt > 2 for cnt in count.values()):
        print("NO")
        return
    
    # Step 3: Create a coloring scheme
    color = ['0'] * n
    last_color = '0'
    
    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            color[i] = last_color
        else:
            last_color = '1' if last_color == '0' else '0'
            color[i] = last_color
    
    print("YES")
    print(''.join(color))

# Example usage:
# n = int(input())
# s = input().strip()
# can_color_string(n, s)