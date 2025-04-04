def minimum_traps(m, x):
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

if __name__ == "__main__":
    m, x = map(int, input("Enter values for m and x, separated by a space: ").split())
    print(minimum_traps(m, x))