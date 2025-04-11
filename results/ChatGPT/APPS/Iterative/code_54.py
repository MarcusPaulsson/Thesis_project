n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    min_a = min(a)
    max_a = max(a)
    
    if max_a == min_a:
        print(0)
    elif max_a - min_a == 1:
        print(1)
    elif (max_a - min_a) % 2 == 0:
        mid = (max_a + min_a) // 2
        if mid in a:
            print((max_a - min_a) // 2)
        else:
            print(-1)
    else:
        print(-1)