def color_array(n, k, a):
    from collections import defaultdict

    color = [0] * n
    freq = defaultdict(list)

    for index, value in enumerate(a):
        freq[value].append(index)

    if len(freq) < k:
        print("NO")
        return

    color_count = [0] * (k + 1)
    current_color = 1

    for indices in freq.values():
        for index in indices:
            color[index] = current_color
            color_count[current_color] += 1
            current_color += 1
            if current_color > k:
                current_color = 1

    if any(c == 0 for c in color_count[1:k + 1]):
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color)))

# Example usage
if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    color_array(n, k, a)