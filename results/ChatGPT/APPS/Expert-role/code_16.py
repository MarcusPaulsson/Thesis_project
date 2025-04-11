cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# A regular bracket sequence can be formed if:
# 1. The total number of opening brackets must be equal to the total number of closing brackets.
# 2. At any point in the sequence, the number of closing brackets must not exceed the number of opening brackets.

# Calculate the total number of opening and closing brackets
open_brackets = cnt1 + cnt2
close_brackets = cnt2 + cnt3

# Check the conditions for a regular bracket sequence
if open_brackets >= close_brackets and (cnt1 - cnt3) >= 0:
    print(1)
else:
    print(0)