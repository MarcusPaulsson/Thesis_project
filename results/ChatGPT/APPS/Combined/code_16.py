def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate total counts of opening and closing brackets
    opening_brackets = cnt1 + cnt2  # Total opening brackets
    closing_brackets = cnt2 + cnt4   # Total closing brackets

    # Check the balance of brackets
    if opening_brackets < closing_brackets:
        return 0

    # Check if we can maintain balance during the sequence
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