def can_deal_exact_damage(a, b, c):
    # Loop through the maximum number of shots from the first gun (Ebony)
    for i in range(c // a + 1):
        # Calculate the remaining damage needed after i shots from Ebony
        remaining_damage = c - i * a
        # Check if remaining damage can be achieved with shots from Ivory
        if remaining_damage >= 0 and remaining_damage % b == 0:
            return "Yes"
    return "No"

# Input reading
a, b, c = map(int, input().split())
print(can_deal_exact_damage(a, b, c))