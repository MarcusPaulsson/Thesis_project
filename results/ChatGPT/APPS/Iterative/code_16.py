cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Calculate the balance of opening and closing brackets
open_brackets = cnt_1 + cnt_2
close_brackets = cnt_3 + cnt_4

# Check if the number of opening and closing brackets can form a regular sequence
if open_brackets == close_brackets and cnt_1 <= cnt_2 + cnt_3:
    print(1)
else:
    print(0)