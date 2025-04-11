def is_favorite_in_sequence(a, b, c):
    if c == 0:
        return a == b
    elif c > 0:
        return a <= b and (b - a) % c == 0
    else:  # c < 0
        return a >= b and (a - b) % abs(c) == 0

# Read input
a, b, c = map(int, input().split())

# Check if b appears in the sequence and print result
if is_favorite_in_sequence(a, b, c):
    print("YES")
else:
    print("NO")