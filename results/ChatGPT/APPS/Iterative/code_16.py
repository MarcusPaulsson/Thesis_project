cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Calculate the balance of opening and closing brackets
open_brackets = cnt_1 + cnt_2
close_brackets = cnt_3 + cnt_4

# Check if the number of opening and closing brackets can balance
if open_brackets < close_brackets:
    print(0)
else:
    # Check if we can maintain a non-negative balance while forming the sequence
    if cnt_3 > open_brackets:
        print(0)
    else:
        # Check if we have enough opening brackets to balance the closing ones
        if cnt_1 < cnt_4:
            print(0)
        else:
            print(1)