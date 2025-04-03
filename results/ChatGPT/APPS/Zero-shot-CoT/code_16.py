cnt_1 = int(input().strip())
cnt_2 = int(input().strip())
cnt_3 = int(input().strip())
cnt_4 = int(input().strip())

# To form a valid bracket sequence:
# - The number of opening brackets must be equal to the number of closing brackets.
# - At no point in the sequence should the number of closing brackets exceed the number of opening brackets.

# Count of opening and closing brackets
opening_brackets = cnt_1 + cnt_2
closing_brackets = cnt_3 + cnt_4

# The total number of opening brackets should be equal to the total number of closing brackets
if opening_brackets == closing_brackets:
    # The number of closing brackets should not exceed the number of opening brackets at any point
    # This can be ensured by checking:
    # The number of closing brackets that can be used at the start of the sequence (cnt_3)
    # should not exceed the number of opening brackets that can be opened before them (cnt_1 + cnt_2)
    if cnt_3 <= opening_brackets:
        print(1)
    else:
        print(0)
else:
    print(0)