cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Calculate total open and close brackets
open_brackets = cnt_1 + cnt_2
close_brackets = cnt_2 + cnt_4

# Check conditions for a regular bracket sequence
if open_brackets >= close_brackets and (open_brackets - close_brackets) <= cnt_3:
    print(1)
else:
    print(0)