def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the balance of opening and closing brackets
    open_needed = cnt1 + cnt2  # Total open brackets available
    close_needed = cnt2 + cnt4  # Total close brackets available

    # The number of opening brackets must be equal to the number of closing brackets
    if open_needed != close_needed:
        return 0

    # The number of extra opening brackets must not exceed the total closing brackets available at any point
    # This ensures that there are enough closing brackets for every opening bracket
    if cnt1 > cnt4 + cnt2:
        return 0

    return 1

# Read input
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))