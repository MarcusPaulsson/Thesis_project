def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - k * (k + 1) // 2

    add = remaining // k
    rem = remaining % k

    for i in range(k):
        a[i] += add

    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1

    
    possible = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            possible = False
            break
    
    if possible:
        print("YES")
        print(*a)
    else:
        
        a = [i + 1 for i in range(k)]
        
        
        if k > 1:
            diff = a[1] - a[0]
            while diff < 1 or a[1]> 2 * a[0]:
                a[0] -= 1
                a[1] += 1
                if a[0] <=0:
                    possible = False
                    break
                diff = a[1] - a[0]
            
            if possible:
                total_sum = sum(a)
                remaining = n - total_sum
                
                add = remaining // k
                rem = remaining % k
                
                for i in range(k):
                    a[i] += add
                
                for i in range(k - 1, k - 1 - rem, -1):
                    a[i] += 1
                    
                possible = True
                for i in range(k - 1):
                    if not (a[i] < a[i+1] <= 2 * a[i]):
                        possible = False
                        break
                if possible:
                    print("YES")
                    print(*a)
                else:
                    print("NO")
            else:
                print("NO")
        else:
            if n > 0:
                print("YES")
                print(n)
            else:
                print("NO")

solve()