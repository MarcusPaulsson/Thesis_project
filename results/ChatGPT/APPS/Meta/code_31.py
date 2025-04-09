def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_paradox(n, k):
    MOD = 1000003
    
    if k > (1 << n):
        return (1, 1)

    total_outcomes = (1 << (n * k))
    favorable_outcomes = 1

    for i in range(k):
        favorable_outcomes *= (1 << n) - i
        favorable_outcomes //= (1 << n)

    A = total_outcomes - favorable_outcomes
    B = total_outcomes

    g = gcd(A, B)
    A //= g
    B //= g

    A %= MOD
    B %= MOD

    return (A, B)

n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])