def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate total open and close brackets
    total_open = cnt1 + cnt2
    total_close = cnt2 + cnt4
    
    # Check if we can balance the brackets
    if total_open < total_close:
        return 0
    
    # Check if we have enough opening brackets to match closing ones
    if cnt1 > cnt4 + cnt2:
        return 0
    
    return 1

# Read input values
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))