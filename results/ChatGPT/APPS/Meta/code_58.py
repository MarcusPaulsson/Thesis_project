def color_array(n, k, a):
    from collections import defaultdict
    
    # Step 1: Create a dictionary to keep track of positions of each number
    positions = defaultdict(list)
    for index, value in enumerate(a):
        positions[value].append(index)
    
    # Step 2: Check if coloring is possible
    # If any number has more than k occurrences, it's impossible to color
    for value in positions.values():
        if len(value) > k:
            print("NO")
            return
    
    # Step 3: Generate coloring
    coloring = [0] * n
    color_used = [0] * (k + 1)  # To track which colors have been used for each number
    current_color = 1
    
    for value in positions:
        for index in positions[value]:
            # Assign the next available color for this number
            coloring[index] = current_color
            color_used[current_color] += 1
            # Move to the next color
            current_color += 1
            if current_color > k:
                current_color = 1
    
    # Step 4: Check if all colors are used
    if all(color_used[i] > 0 for i in range(1, k + 1)):
        print("YES")
        print(" ".join(map(str, coloring)))
    else:
        print("NO")

# Example usage
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)