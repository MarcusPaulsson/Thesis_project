def can_deal_exact_damage(a, b, c):
    if a <= 0 or b <= 0:
        return "No"
    for i in range(c // a + 1):
        if (c - i * a) % b == 0:
            return "Yes"
    return "No"

# Input
a, b, c = map(int, input().split())
# Output
print(can_deal_exact_damage(a, b, c))