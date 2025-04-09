def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 1
    for gcd in range(1, int(n**0.5) + 1):
        if n % gcd == 0:
            if n // gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, gcd)
            if gcd >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // gcd)

    if best_gcd == 1 and k * (k + 1) // 2 > n:
      print(-1)
      return

    
    
    sequence_sum = n // best_gcd
    sequence = []
    for i in range(1, k):
        sequence.append(i)
        sequence_sum -= i
    sequence.append(sequence_sum)

    if sequence[-1] <= sequence[-2]:
        print(-1)
        return

    result = [x * best_gcd for x in sequence]
    print(*result)

solve()