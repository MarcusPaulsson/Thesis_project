def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the total number of opening and closing brackets
    total_opening = cnt1 + cnt2
    total_closing = cnt2 + cnt4
    
    # Check if the number of opening and closing brackets can balance
    if total_opening != total_closing:
        return 0
    
    # Check if we can balance the brackets
    if cnt1 > cnt4 + cnt2:
        return 0
    
    return 1

# Input reading
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))