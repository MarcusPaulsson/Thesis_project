cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Check if it's possible to form a regular bracket sequence
if cnt1 + cnt2 < cnt3 + cnt4:
    print(0)
elif cnt1 > cnt4:
    print(1)
elif cnt1 == cnt4:
    print(1 if cnt2 % 2 == 0 else 0)
else:
    print(0)