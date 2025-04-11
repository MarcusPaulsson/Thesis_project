def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the total number of opening and closing brackets
    total_open = cnt1 + cnt2
    total_close = cnt2 + cnt4
    
    # Check if the number of opening and closing brackets can balance each other
    if total_open < total_close:
        return 0
    
    # Calculate the excess closing brackets
    excess_close = cnt3 + cnt4 - cnt1
    
    # If there are more excess closing brackets than opening brackets, it's not possible
    if excess_close > total_open:
        return 0
    
    return 1

# Read input values
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))