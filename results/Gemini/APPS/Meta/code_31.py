def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 60 and k > mod:
        print(0, 1)
        return

    if k > (1 << min(n, 60)):
        print(1, 1)
        return

    total_days = pow(2, n, mod)
    
    if k > mod:
      num = 0
      den = 1
    else:
      num = 1
      for i in range(k):
          num = (num * (total_days - i)) % mod

      den = pow(total_days, k, mod)
    
    
    if num == 0:
      a = 1
      b = 1
    else:
      
      gcd_val = gcd(num, den)
      num //= gcd_val
      den //= gcd_val

      num %= mod
      den %= mod
      
      a = (den - num + mod) % mod
      b = den % mod
      

    print(a, b)
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()