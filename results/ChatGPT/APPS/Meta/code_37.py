def can_break_shield(a, b, c):
    # Check all possible combinations of shots from Ebony and Ivory
    for x in range(c // a + 1):  # x is the number of shots from Ebony
        remaining_damage = c - a * x
        if remaining_damage >= 0 and remaining_damage % b == 0:
            return "Yes"
    return "No"

# Input
a, b, c = map(int, input().split())
# Output
print(can_break_shield(a, b, c))