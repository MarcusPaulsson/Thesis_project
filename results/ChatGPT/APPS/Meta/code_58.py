def color_array(n, k, a):
    from collections import defaultdict
    
    # Step 1: Count occurrences of each number
    count = defaultdict(int)
    for num in a:
        count[num] += 1
    
    # Step 2: Check if any number occurs more than k times
    for num in count:
        if count[num] > k:
            print("NO")
            return
    
    # Step 3: Prepare to assign colors
    color_assignment = [0] * n
    color_used = defaultdict(int)  # To track how many times each color is used for each number
    
    # Step 4: Assign colors
    for i in range(n):
        num = a[i]
        # Find the next color to assign to this number
        next_color = (color_used[num] % k) + 1
        color_assignment[i] = next_color
        color_used[num] += 1
    
    # Step 5: Check if we have used all colors
    used_colors = set(color_assignment)
    if len(used_colors) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color_assignment)))

# Example usage
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)