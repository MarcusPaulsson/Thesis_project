def can_form_regular_bracket_sequence(cnt_open_open, cnt_open_close, cnt_close_open, cnt_close_close):
    # Calculate the total number of opening and closing brackets
    total_opening = cnt_open_open + cnt_open_close  # Total opening brackets
    total_closing = cnt_open_close + cnt_close_close  # Total closing brackets

    # Ensure the number of opening brackets is at least equal to the number of closing brackets
    if total_opening != total_closing or cnt_open_open < cnt_close_open:
        return 0
    return 1

# Read inputs
cnt_open_open = int(input().strip())
cnt_open_close = int(input().strip())
cnt_close_open = int(input().strip())
cnt_close_close = int(input().strip())

# Print the result
print(can_form_regular_bracket_sequence(cnt_open_open, cnt_open_close, cnt_close_open, cnt_close_close))