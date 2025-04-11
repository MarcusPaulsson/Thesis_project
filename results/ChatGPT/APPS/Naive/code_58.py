def color_array(n, k, a):
    from collections import defaultdict
    
    # Dictionary to keep track of the colors assigned to each number
    color_map = defaultdict(list)
    result = [0] * n
    
    # Assign colors to each element in the array
    for i in range(n):
        num = a[i]
        # Get the current color to assign
        current_color = len(color_map[num]) % k + 1
        color_map[num].append(current_color)
        result[i] = current_color
    
    # Check if we have at least one of each color
    if len(set(result)) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

# Example usage:
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# color_array(n, k, a)