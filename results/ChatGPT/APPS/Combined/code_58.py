def color_array(n, k, a):
    from collections import defaultdict

    # Step 1: Initialize data structures for counting and storing positions
    color_assignment = [0] * n
    element_positions = defaultdict(list)

    # Step 2: Collect positions of each element
    for index, value in enumerate(a):
        element_positions[value].append(index)

    # Step 3: Check if coloring is possible and assign colors
    color = 1
    for positions in element_positions.values():
        if len(positions) > k:
            print("NO")
            return
        
        # Assign colors to the current element
        for pos in positions:
            color_assignment[pos] = color
            color = color + 1 if color < k else 1

    # Step 4: Ensure all colors are used
    if len(set(color_assignment)) < k:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color_assignment)))

# Example usage
if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    color_array(n, k, a)