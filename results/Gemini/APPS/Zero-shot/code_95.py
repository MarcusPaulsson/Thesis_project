def solve():
  n = int(input())
  s = input()
  t = input()

  def check(res, s, t):
    for i in range(len(res) - 1):
      if res[i:i+2] == s or res[i:i+2] == t:
        return False
    return True

  def generate_strings(n):
    chars = ['a', 'b', 'c']
    import itertools
    
    for p in itertools.permutations(chars):
      res1 = p[0] * n + p[1] * n + p[2] * n
      if check(res1, s, t):
        return "YES\n" + res1
      
      res2 = p[0] * n + p[2] * n + p[1] * n
      if check(res2, s, t):
        return "YES\n" + res2

      res3 = p[1] * n + p[0] * n + p[2] * n
      if check(res3, s, t):
        return "YES\n" + res3

      res4 = p[1] * n + p[2] * n + p[0] * n
      if check(res4, s, t):
        return "YES\n" + res4

      res5 = p[2] * n + p[0] * n + p[1] * n
      if check(res5, s, t):
        return "YES\n" + res5

      res6 = p[2] * n + p[1] * n + p[0] * n
      if check(res6, s, t):
        return "YES\n" + res6

    if s == "aa" or t == "aa":
      res = "bc" * n + "a" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "b" * n + "c" * n + "a" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "c" * n + "b" * n + "a" * n
      if check(res, s, t):
        return "YES\n" + res

    if s == "bb" or t == "bb":
      res = "ac" * n + "b" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "a" * n + "c" * n + "b" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "c" * n + "a" * n + "b" * n
      if check(res, s, t):
        return "YES\n" + res

    if s == "cc" or t == "cc":
      res = "ab" * n + "c" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "a" * n + "b" * n + "c" * n
      if check(res, s, t):
        return "YES\n" + res
      res = "b" * n + "a" * n + "c" * n
      if check(res, s, t):
        return "YES\n" + res

    
    if n == 1:
      for p in itertools.permutations(chars):
        res = "".join(p)
        if check(res, s, t):
          return "YES\n" + res
    
    if n <= 3:
      chars_arr = ['a'] * n + ['b'] * n + ['c'] * n
      for p in itertools.permutations(chars_arr):
        res = "".join(p)
        if check(res, s, t):
          return "YES\n" + res

        
    
    return "NO"
  
  print(generate_strings(n))

solve()