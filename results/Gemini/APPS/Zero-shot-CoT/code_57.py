def solve():
  n = int(input())
  f = list(map(int, input().split()))
  
  givers = [i + 1 for i in range(n)]
  receivers = [i + 1 for i in range(n)]
  
  given = set()
  
  for i in range(n):
    if f[i] != 0:
      given.add(f[i])
  
  not_given = []
  for i in range(1, n + 1):
    if i not in given:
      not_given.append(i)
      
  zeros = []
  for i in range(n):
    if f[i] == 0:
      zeros.append(i)
  
  
  for i in range(len(zeros)):
    idx = zeros[i]
    
    candidates = []
    for val in not_given:
      if val != idx + 1:
        candidates.append(val)
    
    if not candidates:
      print("Error: No candidates")
      return
    
    best_candidate = candidates[0]
    
    f[idx] = best_candidate
    not_given.remove(best_candidate)
  
  
  
  print(*f)

solve()