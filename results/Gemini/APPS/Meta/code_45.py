def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 0
    best_seq = []

    for gcd in range(int(n**0.5), 0, -1):
        if n % gcd == 0:
            
            
            def check(cur_gcd):
              
              rem = n // cur_gcd
              if k * (k + 1) // 2 > rem:
                  return False
              
              seq = [i for i in range(1, k)]
              last = rem - sum(seq)
              
              if last <= seq[-1]:
                return False
              
              return True

            if check(gcd):
                rem = n // gcd
                seq = [i for i in range(1, k)]
                last = rem - sum(seq)
                
                seq = [x * gcd for x in seq]
                seq.append(last * gcd)
                
                print(*seq)
                return
            

            def check2(cur_gcd):
              rem = n // cur_gcd
              if k * (k + 1) // 2 > rem:
                  return False
              
              seq = [i for i in range(1, k)]
              last = rem - sum(seq)
              
              if last <= seq[-1]:
                return False
              
              return True

            if check2(n // gcd):
                rem = gcd
                seq = [i for i in range(1, k)]
                last = rem - sum(seq)
                
                seq = [x * (n // gcd) for x in seq]
                seq.append(last * (n // gcd))
                
                print(*seq)
                return

    print("-1")

solve()