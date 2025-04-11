def is_favorite_in_sequence(a, b, c):
    if c == 0:
        return a == b
    elif (b - a) % c == 0 and (b - a) // c >= 0:
        return True
    return False

# Read input
a, b, c = map(int, input().split())

# Check if b is in the sequence and print the result
if is_favorite_in_sequence(a, b, c):
    print("YES")
else:
    print("NO")