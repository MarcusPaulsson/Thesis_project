cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Check if it is possible to form a regular bracket sequence
if cnt1 + cnt2 < cnt3 + cnt4:
    print(0)
else:
    # Check if the excess closing brackets can be balanced
    if cnt3 > cnt1 + cnt2:
        print(0)
    else:
        print(1)