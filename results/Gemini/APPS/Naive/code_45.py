def solve():
    n, k = map(int, input().split())

    if k > 100000:
        print("-1")
        return
    
    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            
            rem = n // gcd
            if rem >= k * (k + 1) // 2:
                seq = [gcd * i for i in range(1, k)]
                seq.append(n - sum(seq))
                
                is_increasing = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
                
                if is_increasing:
                    best_gcd = gcd
                    best_seq = seq
                    break

            rem = gcd
            if rem >= k * (k + 1) // 2:
                
                gcd2 = n // gcd
                seq = [gcd2 * i for i in range(1, k)]
                seq.append(n - sum(seq))
                
                is_increasing = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
                
                if is_increasing:
                    best_gcd = n // gcd
                    best_seq = seq
                    break
    
    if best_gcd == 0:
        print("-1")
    else:
        print(*best_seq)

solve()