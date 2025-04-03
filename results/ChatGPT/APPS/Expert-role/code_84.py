def can_color_string(n, s):
    # Create a list to hold the count of each character
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Check if we can color the string
    color = []
    for i in range(n):
        if i > 0 and s[i] < s[i - 1]:
            # If current character is less than previous, we need to color differently
            if color and color[-1] == '0':
                color.append('1')
            else:
                color.append('0')
        else:
            color.append('0')

    # Check if there are any adjacent characters that are the same but have different colors
    for i in range(1, n):
        if s[i] == s[i - 1] and color[i] != color[i - 1]:
            return "NO"

    return "YES\n" + ''.join(color)


# Read input
n = int(input())
s = input().strip()

# Get the result and print it
result = can_color_string(n, s)
print(result)