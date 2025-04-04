def color_array(n, k, a):
    from collections import defaultdict

    freq = defaultdict(list)

    # Collect indices of each unique element
    for index, value in enumerate(a):
        freq[value].append(index)

    # Check if we can color the array
    if any(len(indices) > k for indices in freq.values()):
        print("NO")
        return

    colors = [0] * n
    current_color = 1

    # Assign colors
    for indices in freq.values():
        for index in indices:
            colors[index] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    print("YES")
    print(" ".join(map(str, colors)))

# Example usage
n, k = map(int, input().split())
a = list(map(int, input().split()))
color_array(n, k, a)