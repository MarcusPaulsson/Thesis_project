def can_break_shield(a, b, c):
    for x in range(c // a + 1):
        if (c - a * x) % b == 0:
            return "Yes"
    return "No"

# Input reading
a, b, c = map(int, input().split())
print(can_break_shield(a, b, c))