def can_color_and_sort(n, s):
    # Count frequencies of each character
    from collections import Counter
    count = Counter(s)
    
    # Check for impossible cases
    for char, freq in count.items():
        if freq > 2:
            return "NO"
    
    # Prepare coloring
    color = []
    for char in s:
        if color.count('0') < count[char] // 2:
            color.append('0')
        else:
            color.append('1')

    return "YES\n" + ''.join(color)

# Reading input
n = int(input())
s = input()

# Getting the result
result = can_color_and_sort(n, s)

# Printing the result
print(result)