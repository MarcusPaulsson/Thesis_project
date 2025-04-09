n = int(input().strip())
s = input().strip()

# Create a dictionary to count occurrences of each character
from collections import defaultdict

char_count = defaultdict(int)
for char in s:
    char_count[char] += 1

# Check if we can color the string
max_count = max(char_count.values())

# If any character appears more than (n + 1) // 2 times, it's impossible to color
if max_count > (n + 1) // 2:
    print("NO")
else:
    print("YES")
    coloring = []
    color = 0
    for char in s:
        # Assign color based on the current character's count
        if char_count[char] > 0:
            coloring.append(str(color))
            char_count[char] -= 1
            # Toggle color for next character
            color ^= 1
        else:
            coloring.append(str(color ^ 1))  # Alternate color if this character is exhausted

    print(''.join(coloring))