n = int(input().strip())
s = input().strip()

# To check the conditions for coloring
color = [''] * n
last_position = {}
possible = True

for i in range(n):
    if s[i] in last_position:
        # If the character has appeared before, check if we can assign the same color
        color[i] = '0' if color[last_position[s[i]]] == '1' else '1'
    else:
        # Assign the first color '0' if it's the first occurrence
        color[i] = '0'
    
    last_position[s[i]] = i

# Check if the string can be sorted with the current coloring
for i in range(n - 1):
    if s[i] > s[i + 1] and color[i] == color[i + 1]:
        possible = False
        break

print("YES" if possible else "NO")
if possible:
    print(''.join(color))