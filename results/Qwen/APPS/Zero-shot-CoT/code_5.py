def min_seconds_to_close_tabs(n, pos, l, r):
    if pos < l:
        return l - pos + (n - r)
    elif pos > r:
        return pos - r + (l - 1)
    else:
        return max(pos - l, r - pos)

n, pos, l, r = map(int, input().split())
print(min_seconds_to_close_tabs(n, pos, l, r))