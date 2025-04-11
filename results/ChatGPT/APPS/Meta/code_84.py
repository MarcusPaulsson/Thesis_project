n = int(input())
s = input()

# Create a list to store the color assignments
color = ['0'] * n

# Create a list to track the last seen index of each character
last_seen = {}

# Iterate through the string
for i in range(n):
    char = s[i]
    if char in last_seen:
        # If the character has been seen before, we need to check the last index
        last_index = last_seen[char]
        # If the last index is colored differently, we can't sort it
        if color[last_index] == color[i]:
            print("NO")
            exit()
    # Update the last seen index for the character
    last_seen[char] = i
    # Alternate colors for different characters
    color[i] = '0' if color[i-1] == '1' else '1' if i > 0 else '0'

print("YES")
print(''.join(color))