def color_array(n, k, a):
    from collections import defaultdict

    color = [0] * n
    freq = defaultdict(list)

    # Collect indices for each unique number
    for i in range(n):
        freq[a[i]].append(i)

    # Check if we can color the array
    if any(len(indices) > k for indices in freq.values()):
        print("NO")
        return

    # Assign colors
    current_color = 1
    for indices in freq.values():
        for index in indices:
            color[index] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    print("YES")
    print(" ".join(map(str, color)))

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

color_array(n, k, a)