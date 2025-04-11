def can_color_string(n, s):
    from collections import Counter

    # Step 1: Count occurrences of each character
    count = Counter(s)

    # Step 2: Check if any character occurs more than twice
    if any(cnt > 2 for cnt in count.values()):
        return "NO", ""

    # Step 3: Create a coloring scheme
    color = []
    for char in s:
        # Determine color based on the count of '0's and '1's used
        if color.count('0') < (count[char] + 1) // 2:
            color.append('0')
        else:
            color.append('1')

    return "YES", ''.join(color)

# Input reading
n = int(input())
s = input().strip()

# Get the result
result, coloring = can_color_string(n, s)

# Output the result
print(result)
if result == "YES":
    print(coloring)