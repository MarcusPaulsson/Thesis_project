cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# Check the conditions for forming a regular bracket sequence
if cnt1 + cnt2 >= cnt3 + cnt4 and cnt3 <= cnt1 + cnt2:
    print(1)
else:
    print(0)