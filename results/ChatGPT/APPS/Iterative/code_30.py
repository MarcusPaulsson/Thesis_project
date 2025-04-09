def minimum_traps(m, x):
    # Since GCD(x, m) = 1, the x-mouse will visit φ(m) distinct rooms
    # We can place traps in all of these distinct rooms to ensure the mouse is caught.
    
    def euler_totient(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result
    
    return euler_totient(m)

m, x = map(int, input().split())
print(minimum_traps(m, x))