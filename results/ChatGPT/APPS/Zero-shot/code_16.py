cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Calculate the balance of opening and closing brackets
open_needed = cnt1 + cnt2  # Total opening brackets needed
close_needed = cnt3 + cnt4  # Total closing brackets needed

# Check if we can form a regular bracket sequence
if open_needed == close_needed and cnt1 <= cnt4 + cnt2:
    print(1)
else:
    print(0)