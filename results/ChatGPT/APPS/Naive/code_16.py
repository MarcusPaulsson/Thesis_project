def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the number of opening and closing brackets needed
    open_needed = cnt1 + cnt2
    close_needed = cnt3 + cnt4

    # Check if the counts match for a valid sequence
    if open_needed == close_needed:
        # Check if the number of ')' does not exceed the number of '(' at any point
        if cnt3 <= cnt1 + cnt2: 
            return 1
    return 0

# Read inputs
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))