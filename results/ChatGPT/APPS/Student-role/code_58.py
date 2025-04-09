def color_array(n, k, a):
    from collections import defaultdict

    color_assignment = [0] * n
    freq = defaultdict(list)

    # Collect indices of each element in the array
    for index, value in enumerate(a):
        freq[value].append(index)

    # Check if it's possible to color
    if any(len(indices) > k for indices in freq.values()):
        print("NO")
        return

    # Assign colors
    color = 1
    for indices in freq.values():
        for idx in indices:
            color_assignment[idx] = color
            color += 1
            if color > k:
                color = 1

    print("YES")
    print(' '.join(map(str, color_assignment)))

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))

color_array(n, k, a)