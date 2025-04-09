def solve():
  n, m = map(int, input().split())

  if n == m:
    print(0)
    return

  if m % n != 0:
    print(-1)
    return

  div = m // n
  
  count = 0
  while div % 2 == 0:
    div //= 2
    count += 1
  while div % 3 == 0:
    div //= 3
    count += 1
  
  if div != 1:
    print(-1)
  else:
    twos = 0
    threes = 0
    temp = m // n
    while temp % 2 == 0:
        temp //= 2
        twos += 1
    while temp % 3 == 0:
        temp //= 3
        threes += 1
    
    if (2**twos) * (3**threes) == m//n:
        print(twos + threes)
    
solve()