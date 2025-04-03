def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    current_sum = sum(a)
    diff = n - current_sum

    if diff == 0:
        print("YES")
        print(*a)
        return

    add = diff // k
    rem = diff % k

    for i in range(k):
        a[i] += add

    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1

    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            
            found = False
            for start in range(k):
                temp_a = [i + 1 for i in range(k)]
                current_sum = sum(temp_a)
                diff = n - current_sum

                add = diff // k
                rem = diff % k
                
                for i in range(k):
                    temp_a[i] += add
                    
                for i in range(k - 1, k - 1 - rem, -1):
                    temp_a[i] += 1
                
                valid = True
                for i in range(k - 1):
                    if not (temp_a[i] < temp_a[i+1] <= 2 * temp_a[i]):
                        valid = False
                        break
                
                if valid:
                    print("YES")
                    print(*temp_a)
                    return
                
                
            print("NO")
            return
            

    print("YES")
    print(*a)

solve()