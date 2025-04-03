cnt1 = int(input().strip())
cnt2 = int(input().strip())
cnt3 = int(input().strip())
cnt4 = int(input().strip())

# Total open and close brackets
open_brackets = cnt1 + cnt2
close_brackets = cnt3 + cnt4

# Condition for a regular bracket sequence
if open_brackets >= close_brackets and (open_brackets - close_brackets) <= cnt2:
    print(1)
else:
    print(0)