def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the total number of opening and closing brackets
    open_brackets = cnt1 + cnt2
    close_brackets = cnt2 + cnt3
    
    # Check if the number of opening and closing brackets can balance
    if open_brackets < close_brackets:
        return 0
    
    # Check if the excess closing brackets can be balanced by opening brackets
    excess_closing = cnt3 - cnt1
    if excess_closing > 0 and excess_closing > cnt2:
        return 0
    
    return 1

# Read input values
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))