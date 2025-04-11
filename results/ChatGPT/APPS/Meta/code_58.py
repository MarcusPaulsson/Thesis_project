def color_array(n, k, a):
    from collections import defaultdict

    color_assignment = [0] * n
    color_count = defaultdict(int)
    color_used = defaultdict(set)

    for i in range(n):
        value = a[i]
        if color_count[value] < k:
            color_count[value] += 1
            color_assignment[i] = color_count[value]
            color_used[color_count[value]].add(value)
        else:
            # Try to assign a color that has not been used for this value
            for color in range(1, k + 1):
                if value not in color_used[color]:
                    color_assignment[i] = color
                    color_used[color].add(value)
                    break

    # Check if we have used all colors at least once
    if len(color_used) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color_assignment)))

# Example usage
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# color_array(n, k, a)