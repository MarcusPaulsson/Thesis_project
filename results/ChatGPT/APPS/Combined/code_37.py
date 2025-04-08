def can_break_shield(a, b, c):
    # Iterate over the possible number of shots from the Ebony gun
    for shots_from_ebony in range(c // a + 1):
        remaining_damage = c - a * shots_from_ebony
        # Check if the remaining damage can be dealt by the Ivory gun
        if remaining_damage >= 0 and remaining_damage % b == 0:
            return "Yes"
    return "No"

# Read input values
a, b, c = map(int, input().split())
# Output the result
print(can_break_shield(a, b, c))