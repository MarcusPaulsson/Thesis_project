cnt_1 = int(input())
cnt_2 = int(input())
cnt_3 = int(input())
cnt_4 = int(input())

# Count of opening and closing brackets
opening = cnt_1 + cnt_2  # "(", "()" contribute to opening
closing = cnt_2 + cnt_4   # "()", "))" contribute to closing

# Check if we can form a regular bracket sequence
if opening >= closing and (opening - closing) <= cnt_3:
    print(1)
else:
    print(0)