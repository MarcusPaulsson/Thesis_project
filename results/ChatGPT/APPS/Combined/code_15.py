def is_favorite_in_sequence(a, b, c):
    if c == 0:
        return a == b
    return (b - a) % c == 0 and (b - a) // c >= 0

# Input reading
a, b, c = map(int, input().split())

# Output result
print("YES" if is_favorite_in_sequence(a, b, c) else "NO")