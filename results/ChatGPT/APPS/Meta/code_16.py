def can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4):
    # A regular bracket sequence can be formed if:
    # 1. The number of opening brackets can match the number of closing brackets.
    # 2. At any point in the sequence, the number of closing brackets should not exceed the number of opening brackets.
    
    # Calculate the balance of opening and closing brackets
    open_count = cnt1 + cnt2  # Opening brackets from "((" and "()"
    close_count = cnt3 + cnt4  # Closing brackets from ")(" and "))"
    
    # Check if there are enough opening brackets to match the closing brackets
    if open_count < close_count:
        return 0
    
    # Calculate the excess opening and closing brackets
    excess_open = cnt1 - cnt4  # Excess opening that needs to be matched
    excess_close = cnt3  # Closing brackets that can be used
    
    # We need to ensure that the excess opening brackets can be matched by the closing brackets
    if excess_open < 0:
        return 0
    
    return 1

# Read input
cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Output the result
print(can_form_regular_bracket_sequence(cnt1, cnt2, cnt3, cnt4))