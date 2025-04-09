def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            divisors = [gcd, n // gcd]
            for q in divisors:
                if q >= k * (k + 1) // 2:
                    remaining_sum = q - k * (k + 1) // 2
                    seq = [i + 1 for i in range(k)]
                    seq[-1] += remaining_sum
                    
                    valid = True
                    for i in range(k - 1):
                        if seq[i] >= seq[i+1]:
                            valid = False
                            break
                    
                    if valid:
                        current_gcd = n // q
                        seq = [x * current_gcd for x in seq]
                        
                        if best_gcd == 0 or current_gcd > best_gcd:
                            best_gcd = current_gcd
                            best_seq = seq
                            

    if best_gcd == 0:
        if n == 1 and k == 1:
            print(1)
        else:
            print("-1")
    else:
        print(*best_seq)

solve()