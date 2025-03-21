def solve():
  n = int(input())
  a = list(map(int, input().split()))

  def get_k_amazing_number(k):
    candidates = set(a)
    
    possible_amazing_numbers = []
    
    for num in candidates:
        is_amazing = True
        for i in range(n - k + 1):
            subsegment = a[i:i+k]
            if num not in subsegment:
                is_amazing = False
                break
        if is_amazing:
            possible_amazing_numbers.append(num)
            
    if not possible_amazing_numbers:
        return -1
    else:
        return min(possible_amazing_numbers)

  result = []
  for k in range(1, n + 1):
    result.append(get_k_amazing_number(k))

  print(*result)

t = int(input())
for _ in range(t):
  solve()