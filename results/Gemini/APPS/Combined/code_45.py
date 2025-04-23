def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            q = n // gcd
            
            # Check if gcd is a valid GCD
            if q >= k * (k + 1) // 2:
                seq = [gcd * i for i in range(1, k)]
                seq.append(n - sum(seq))
                
                if all(seq[i] < seq[i+1] for i in range(len(seq)-1)) and all(x > 0 for x in seq):
                    print(*seq)
                    return
            
            # Check if q is a valid GCD
            if gcd != q:
                if gcd >= k * (k + 1) // 2:
                    continue
                if q >= k * (k + 1) // 2:
                    seq = [q * i for i in range(1, k)]
                    seq.append(n - sum(seq))
                    
                    if all(seq[i] < seq[i+1] for i in range(len(seq)-1)) and all(x > 0 for x in seq):
                        print(*seq)
                        return

    if n == 1 and k == 1:
        print(1)
        return

    print("-1")

solve()