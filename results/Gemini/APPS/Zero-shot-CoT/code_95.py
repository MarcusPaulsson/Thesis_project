def solve():
  n = int(input())
  s = input()
  t = input()

  def check(res, s, t):
    for i in range(len(res) - 1):
      if res[i:i+2] == s or res[i:i+2] == t:
        return False
    return True
  
  def find_string(n, s, t):
    chars = ['a', 'b', 'c']
    import itertools
    
    for perm in itertools.permutations(chars):
      res1 = perm[0] * n + perm[1] * n + perm[2] * n
      if check(res1, s, t):
        return res1
        
      res2 = perm[0] * n + perm[2] * n + perm[1] * n
      if check(res2, s, t):
        return res2

    return None

  res = find_string(n, s, t)

  if res:
    print("YES")
    print(res)
  else:
    print("NO")

solve()