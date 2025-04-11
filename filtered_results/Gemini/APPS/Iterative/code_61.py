def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    best_a = list(a)
    
    start = -1
    end = -1
    
    for i in range(n):
        digit = int(a[i])
        if f[digit - 1] > digit:
            start = i
            break
    
    if start != -1:
        end = start
        for i in range(start, n):
            digit = int(a[i])
            if f[digit - 1] >= digit:
                end = i
            else:
                break
        
        for i in range(start, end + 1):
            digit = int(a[i])
            best_a[i] = str(f[digit - 1])
    
    print("".join(best_a))

solve()