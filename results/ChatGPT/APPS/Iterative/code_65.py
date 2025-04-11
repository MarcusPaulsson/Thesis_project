n, m = map(int, input().split())

if m % n != 0:
    print(-1)
else:
    ratio = m // n
    count_2 = 0
    count_3 = 0
    
    while ratio % 2 == 0:
        ratio //= 2
        count_2 += 1
    
    while ratio % 3 == 0:
        ratio //= 3
        count_3 += 1
    
    if ratio == 1:
        print(count_2 + count_3)
    else:
        print(-1)