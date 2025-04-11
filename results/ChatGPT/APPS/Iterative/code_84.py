n = int(input())
s = input().strip()

# Count occurrences of each character
from collections import Counter
count = Counter(s)

# Check if we can color the string
coloring = ['0'] * n
last_color = '0'

for i in range(n):
    if i > 0 and s[i] == s[i - 1]:
        coloring[i] = coloring[i - 1]
    else:
        # Alternate colors
        last_color = '1' if last_color == '0' else '0'
        coloring[i] = last_color

# Check if the coloring is valid
for char in count:
    if count[char] > 1:
        # Check if we can separate the same characters
        positions = [i for i in range(n) if s[i] == char]
        if len(set(coloring[i] for i in positions)) == 1:
            print("NO")
            exit()

print("YES")
print(''.join(coloring))