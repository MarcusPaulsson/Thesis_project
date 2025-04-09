def color_array(n, k, a):
    from collections import defaultdict
    
    # Step 1: Initialize variables
    color_assignment = [0] * n
    color_used = defaultdict(set)
    color_count = [0] * (k + 1)
    
    # Step 2: Assign colors
    for i in range(n):
        num = a[i]
        for color in range(1, k + 1):
            # If this color has not been used for this number
            if num not in color_used[color]:
                color_assignment[i] = color
                color_used[color].add(num)
                color_count[color] += 1
                break
    
    # Step 3: Check if all colors are used
    if all(count > 0 for count in color_count[1:k + 1]):
        print("YES")
        print(" ".join(map(str, color_assignment)))
    else:
        print("NO")

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)