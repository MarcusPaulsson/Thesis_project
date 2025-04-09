n = int(input())
s = input()

# Count occurrences of each character
from collections import Counter
count = Counter(s)

# Check for the maximum frequency of any character
max_freq = max(count.values())

# If max frequency is greater than (n + 1) // 2, it's impossible to color
if max_freq > (n + 1) // 2:
    print("NO")
else:
    print("YES")
    # Generate coloring
    coloring = ['0'] * n
    # Fill in the first half with '0' and the second half with '1'
    half = (n + 1) // 2
    used = Counter()
    
    for i in range(n):
        if used[s[i]] < count[s[i]] // 2:
            coloring[i] = '0'
        else:
            coloring[i] = '1'
        used[s[i]] += 1
    
    print(''.join(coloring))