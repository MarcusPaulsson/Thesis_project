cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Check balance conditions
open_brackets = cnt1 + cnt2
close_brackets = cnt3 + cnt4

# Regular bracket sequence condition
if open_brackets >= close_brackets and cnt1 <= cnt3 + cnt2:
    print(1)
else:
    print(0)