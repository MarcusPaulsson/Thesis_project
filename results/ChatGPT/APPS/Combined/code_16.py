def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # Calculate the total number of opening and closing brackets
    opening_brackets = cnt1 + cnt2
    closing_brackets = cnt2 + cnt4
    
    # Check if the number of opening and closing brackets can form a regular sequence
    if opening_brackets >= closing_brackets and (opening_brackets - closing_brackets) <= cnt3:
        return 1
    return 0

# Read input values
cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))