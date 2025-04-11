cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Check if it's possible to form a regular bracket sequence
if cnt1 + cnt2 >= cnt3 + cnt4 and cnt1 <= cnt3 + 1:
    print(1)
else:
    print(0)