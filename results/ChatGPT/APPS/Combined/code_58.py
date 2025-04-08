def color_array(n, k, a):
    from collections import defaultdict

    # Step 1: Create a mapping of values to their indices
    color_map = defaultdict(list)
    
    # Step 2: Fill the color_map with indices of each unique element
    for index, value in enumerate(a):
        color_map[value].append(index)
        
    # Step 3: Check if the number of unique elements exceeds the available colors
    if len(color_map) > k:
        print("NO")
        return
    
    # Step 4: Prepare the coloring array
    coloring = [0] * n
    current_color = 1
    color_count = 0
    
    # Step 5: Assign colors to elements ensuring distinct elements have distinct colors
    for indices in color_map.values():
        for idx in indices:
            coloring[idx] = current_color
        current_color += 1
        color_count += 1
        
        # Reset color if we exceed k
        if current_color > k:
            current_color = 1
            
    # Step 6: Ensure all colors from 1 to k are used
    if color_count < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, coloring)))

# Example usage:
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)