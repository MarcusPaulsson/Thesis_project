def clean_string(n, s):
    # Count the number of 1's and 0's
    count_0 = s.count('0')
    count_1 = s.count('1')
    
    # Create the cleanest string
    if count_0 == 0:
        return '1'
    elif count_1 == 0:
        return '0'
    else:
        return '0' * 1 + '1' * count_1

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(clean_string(n, s))