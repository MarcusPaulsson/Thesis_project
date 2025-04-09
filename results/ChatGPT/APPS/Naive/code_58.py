def color_array(n, k, a):
    from collections import defaultdict
    
    # Track the frequency of each number
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1
    
    # If the maximum frequency of any number exceeds the number of colors, it's impossible
    max_freq = max(freq.values())
    if max_freq > k:
        print("NO")
        return
    
    # Prepare to store the coloring result
    coloring = [0] * n
    color_used = defaultdict(int)
    
    # Assign colors
    for i in range(n):
        num = a[i]
        # Use a color not used for this number yet
        color_used[num] += 1
        coloring[i] = color_used[num]
        
        # If we exceed the number of colors, reset to 1
        if color_used[num] > k:
            color_used[num] = 1
    
    print("YES")
    print(" ".join(map(str, coloring)))

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function
color_array(n, k, a)