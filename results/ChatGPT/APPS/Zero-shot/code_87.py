def can_deal_exact_damage(a, b, c):
    for i in range(c // a + 1):
        if (c - i * a) % b == 0:
            return "Yes"
    return "No"

# Input reading
a, b, c = map(int, input().split())
print(can_deal_exact_damage(a, b, c))