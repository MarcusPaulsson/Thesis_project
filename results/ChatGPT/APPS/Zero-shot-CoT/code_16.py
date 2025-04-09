cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Check if the number of opening brackets can match the closing brackets.
if cnt_1 + cnt_2 < cnt_3 + cnt_4:
    print(0)
else:
    # Check if we have enough closing brackets to match extra opening brackets.
    if cnt_1 + cnt_2 >= cnt_3 and cnt_4 <= cnt_1:
        print(1)
    else:
        print(0)