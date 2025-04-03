cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Calculate the balance of open and close brackets
open_brackets = cnt_1 + cnt_2
close_brackets = cnt_3 + cnt_4

# Check if the total number of openings and closings can form a regular sequence
if open_brackets == close_brackets:
    # Check if we can maintain a valid sequence throughout
    if cnt_1 + cnt_2 >= cnt_4:
        print(1)
    else:
        print(0)
else:
    print(0)