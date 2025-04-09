def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 1
    for gcd in range(1, int(n**0.5) + 1):
        if n % gcd == 0:
            if n // gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, gcd)
            if gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // gcd)
                
    
    if best_gcd == 1:
        temp_sum = k*(k+1)//2
        if temp_sum > n:
            print("-1")
            return
    
    a = []
    current_sum = 0
    for i in range(1, k):
        a.append(best_gcd * i)
        current_sum += best_gcd * i

    a.append(best_gcd * (n // best_gcd) - current_sum)

    if a[-1] <= a[-2]:
       
        print("-1")
        return
        


    print(*a)

solve()