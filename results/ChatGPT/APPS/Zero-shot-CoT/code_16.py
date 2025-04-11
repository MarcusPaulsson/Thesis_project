cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Check the conditions for forming a regular bracket sequence
if cnt_1 + cnt_2 >= cnt_3 + cnt_4 and cnt_3 <= cnt_1 + cnt_2:
    print(1)
else:
    print(0)