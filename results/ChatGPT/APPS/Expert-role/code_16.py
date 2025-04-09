cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# A regular bracket sequence can be formed if:
# The number of opening brackets can match the closing brackets
# The number of opening brackets must be at least as many as the closing brackets at any point in the sequence.

# Count the total number of opening and closing brackets
total_open = cnt_1 + cnt_2
total_close = cnt_2 + cnt_4

# To be a regular bracket sequence, the total number of open brackets must equal the total number of close brackets,
# and at any point, the number of closing brackets must not exceed the number of opening brackets.
if total_open >= total_close and (cnt_1 + cnt_2 >= cnt_3 + cnt_4):
    print(1)
else:
    print(0)