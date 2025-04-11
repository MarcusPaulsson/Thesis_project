def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    num = 1
    den = 1
    twos = 0

    for i in range(k):
        if i == 0:
            continue

        val = pow(2, n, mod) - i
        if val < 0:
            val += mod

        num = (num * val) % mod
        
        temp = i
        while temp > 0 and temp % 2 == 0:
            twos += 1
            temp //= 2

    
    twos_in_den = min(n * (k - 1), twos)
    
    den = pow(pow(2, n, mod), k - 1, mod)
    twos_in_num = twos
    
    num_twos_removed = 0
    den_twos_removed = 0

    while num != 0 and num % 2 == 0:
      num //= 2
      num_twos_removed += 1
    while den != 0 and den % 2 == 0:
      den //= 2
      den_twos_removed += 1
    
    inv_den = pow(den, mod - 2, mod)
    
    prob_diff = (num * inv_den) % mod

    ans = (1 - prob_diff + mod) % mod

    print(ans, 1)

solve()