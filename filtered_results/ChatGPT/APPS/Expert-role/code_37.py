def can_deal_exact_damage(a, b, c):
    for x in range(c // a + 1):
        if (c - a * x) % b == 0:
            return "Yes"
    return "No"

a, b, c = map(int, input().split())
print(can_deal_exact_damage(a, b, c))