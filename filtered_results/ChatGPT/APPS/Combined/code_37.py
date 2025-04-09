def can_deal_exact_damage(a, b, c):
    # Iterate through the possible number of shots from gun Ebony
    for shots_from_ebony in range(c // a + 1):
        remaining_damage = c - a * shots_from_ebony
        # Check if the remaining damage can be exactly dealt with gun Ivory
        if remaining_damage >= 0 and remaining_damage % b == 0:
            return "Yes"
    return "No"

# Read input
a, b, c = map(int, input().split())
# Call the function and print the result
print(can_deal_exact_damage(a, b, c))