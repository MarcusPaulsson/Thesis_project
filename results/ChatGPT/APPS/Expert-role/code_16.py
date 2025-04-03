cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# A regular bracket sequence can be formed if:
# 1. The number of closing brackets must not exceed the number of opening brackets at any point.
# 2. At the end, the total number of opening brackets must equal the total number of closing brackets.

# The total opening brackets from ( and ) pairs
total_opening = cnt1 + cnt2
# The total closing brackets from ) and ( pairs
total_closing = cnt3 + cnt4

# The count of unbalanced opening and closing brackets
needed_opening = cnt3
needed_closing = cnt1

# Check if we can balance the brackets
if needed_opening <= total_opening and needed_closing <= total_closing and (total_opening - needed_opening) >= needed_closing:
    print(1)
else:
    print(0)