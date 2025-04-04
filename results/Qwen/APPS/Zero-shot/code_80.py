def min_colors_to_sort(s):
    n = len(s)
    colors = [1] * n
    res = 1
    for i in range(1, n):
        if s[i] < s[i - 1]:
            res += 1
            colors[i] = res
    return res, colors

n = int(input())
s = input()
res, colors = min_colors_to_sort(s)
print(res)
print(*colors)