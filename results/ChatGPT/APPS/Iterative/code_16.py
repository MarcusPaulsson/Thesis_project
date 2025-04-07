cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Regular bracket sequence conditions
if cnt1 + cnt2 + cnt3 + cnt4 == 0:
    print(1)
else:
    open_needed = cnt1 + cnt2
    close_needed = cnt3 + cnt4
    
    # Check if we can match the opening and closing brackets
    if open_needed >= close_needed and (open_needed - close_needed) % 2 == 0:
        print(1)
    else:
        print(0)