def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    import sys
    input = sys.stdin.read
    n, k = map(int, input().strip().split())

    MOD = 1000003
    days = 1 << n  # 2^n

    if k > days:
        print(1, 1)
        return

    # Calculate the probability of at least two having the same birthday
    # P(at least two share a birthday) = 1 - P(no one shares a birthday)
    
    # P(no one shares a birthday) = days / days * (days - 1) / days * ... * (days - k + 1) / days
    # = (days * (days - 1) * ... * (days - k + 1)) / days^k
    # = (days * (days - 1) * ... * (days - k + 1)) / (days^k)

    P_no_shared = 1
    for i in range(k):
        P_no_shared *= (days - i)
        P_no_shared %= MOD

    P_no_shared = (P_no_shared * pow(days, MOD - 2, MOD)) % MOD  # Modular inverse of days^k

    # P(shared) = 1 - P(no shared)
    P_shared = (1 - P_no_shared) % MOD

    # P(shared) = A / B
    A = P_shared
    B = 1
    # Find the denominator B
    for i in range(k):
        B *= days
        B %= MOD

    # A = B - P(no shared)
    A = (B - P_no_shared + MOD) % MOD

    # Reduce A and B by their gcd
    g = gcd(A, B)
    A //= g
    B //= g

    print(A, B)

if __name__ == "__main__":
    main()