cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# A regular bracket sequence can be formed if:
# 1. The number of closing brackets (from ")(" and "))") must not exceed the number of opening brackets (from "((" and "()").
# 2. The total number of opening brackets must equal the total number of closing brackets.

# Calculating the number of opening and closing brackets
opening_brackets = cnt_1 + cnt_2
closing_brackets = cnt_3 + cnt_4

# A valid regular bracket sequence can be formed if the following conditions hold:
if opening_brackets >= closing_brackets and (cnt_2 + cnt_1) >= cnt_3:
    print(1)
else:
    print(0)