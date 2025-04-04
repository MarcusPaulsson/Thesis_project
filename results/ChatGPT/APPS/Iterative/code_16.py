def is_regular_bracket_sequence_valid(cnt_1, cnt_2, cnt_3, cnt_4):
    open_needed = cnt_1 + cnt_2  # Opening brackets from "((" and "()"
    close_needed = cnt_2 + cnt_4  # Closing brackets from "() and "))"

    # Check if closing brackets exceed opening brackets
    if close_needed > open_needed:
        return 0

    # Check if unmatched open brackets exceed unmatched close brackets
    if cnt_3 > open_needed:
        return 0

    return 1

# Read input counts
try:
    cnt_1 = int(input("Enter count of '((': "))
    cnt_2 = int(input("Enter count of '()': "))
    cnt_3 = int(input("Enter count of ')(': "))
    cnt_4 = int(input("Enter count of ')): ' "))
    
    # Validate input
    if any(count < 0 for count in (cnt_1, cnt_2, cnt_3, cnt_4)):
        print("Counts must be non-negative.")
    else:
        print(is_regular_bracket_sequence_valid(cnt_1, cnt_2, cnt_3, cnt_4))
except ValueError:
    print("Invalid input. Please enter integers.")