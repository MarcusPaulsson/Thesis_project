a, b, c = map(int, input().split())

def can_deal_exact_damage(a, b, c):
    for i in range(c // a + 1):
        if (c - i * a) % b == 0:
            return True
    return False

if can_deal_exact_damage(a, b, c):
    print("Yes")
else:
    print("No")