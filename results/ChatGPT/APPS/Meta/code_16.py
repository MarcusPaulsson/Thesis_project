cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# To form a regular bracket sequence:
# 1. The number of opening brackets must be equal to the number of closing brackets.
# 2. The number of closing brackets cannot exceed the number of opening brackets at any point.

# Calculate the total number of opening and closing brackets
open_brackets = cnt1 + cnt2
close_brackets = cnt3 + cnt4

# Check the conditions for a regular bracket sequence
if open_brackets >= close_brackets and (cnt1 + cnt2) >= (cnt3):
    print(1)
else:
    print(0)