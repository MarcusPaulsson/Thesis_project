def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    a1, b1, a2, b2, L, R = map(int, input().split())
    
    g, x, y = extended_gcd(a1, a2)
    
    if (b2 - b1) % g != 0:
        print(0)
        return
    
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g
    
    lcm = (a1 * a2) // g
    
    k = x
    l = -y
    
    first_solution = a1 * k + b1
    
    
    k0 = k
    l0 = l
    
    
    k_shift = a2 // g
    l_shift = a1 // g
    
    
    def find_min_k(k_start, a1, a2, b1, b2, L, lcm):
        k = k_start
        while True:
            val = a1 * k + b1
            if val >= L:
                return k
            k += a2 // g
            if k > 10**10:
                return float('inf')
                
    def find_max_k(k_start, a1, a2, b1, b2, R, lcm):
        k = k_start
        while True:
            val = a1 * k + b1
            if val <= R:
                return k
            k -= a2 // g
            if k < -10**10:
                return float('-inf')

    min_k = find_min_k(k0, a1, a2, b1, b2, L, lcm)
    max_k = find_max_k(k0, a1, a2, b1, b2, R, lcm)

    if min_k == float('inf') or max_k == float('-inf') or min_k > max_k:
        print(0)
        return

    
    
    first_val = a1 * min_k + b1

    
    
    count = 0
    curr = first_val
    while curr <= R:
        
        k_val = (curr - b1) // a1
        l_val = (curr - b2) // a2

        if k_val >= 0 and l_val >= 0 and curr >= L:
                count += 1
        curr += lcm

    print(count)

solve()