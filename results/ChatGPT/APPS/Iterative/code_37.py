def can_deal_exact_damage(a, b, c):
    for i in range(c // a + 1):
        if (c - a * i) >= 0 and (c - a * i) % b == 0:
            return "Yes"
    return "No"

a, b, c = map(int, input().split())
print(can_deal_exact_damage(a, b, c))