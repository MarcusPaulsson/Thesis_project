def solve():
    n = int(input())
    s = input()

    def check(arr, color_assignment):
        colored_chars = []
        for i in range(n):
            colored_chars.append((arr[i], color_assignment[i]))

        chars_list = list(s)

        for _ in range(n * (n - 1) // 2):
            swapped = False
            for i in range(n - 1):
                if chars_list[i] > chars_list[i + 1] and color_assignment[i] != color_assignment[i + 1]:
                    chars_list[i], chars_list[i + 1] = chars_list[i + 1], chars_list[i]
                    swapped = True
            if not swapped:
                break

        return "".join(chars_list) == "".join(sorted(s))

    def find_min_colors():
        for num_colors in range(1, n + 1):
            import itertools
            for color_assignment in itertools.product(range(1, num_colors + 1), repeat=n):
                if check(s, list(color_assignment)):
                    return num_colors, list(color_assignment)
        return n, list(range(1, n + 1))

    num_colors, color_assignment = find_min_colors()
    print(num_colors)
    print(*color_assignment)

solve()