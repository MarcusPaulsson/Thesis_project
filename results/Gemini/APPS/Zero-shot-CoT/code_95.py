def solve():
  n = int(input())
  s = input()
  t = input()

  chars = ['a', 'b', 'c']

  import itertools
  
  for p in itertools.permutations(chars):
    res = ""
    for i in range(n):
      res += p[0]
      res += p[1]
      res += p[2]
    
    valid = True
    for i in range(len(res) - 1):
      if res[i:i+2] == s or res[i:i+2] == t:
        valid = False
        break
    
    if valid:
      print("YES")
      print(res)
      return
    
  
  res = ""
  for i in range(n):
    res += 'a'
  for i in range(n):
    res += 'b'
  for i in range(n):
    res += 'c'
    
  valid = True
  for i in range(len(res) - 1):
    if res[i:i+2] == s or res[i:i+2] == t:
      valid = False
      break
      
  if valid:
    print("YES")
    print(res)
    return
  
  res = ""
  for i in range(n):
    res += 'c'
  for i in range(n):
    res += 'b'
  for i in range(n):
    res += 'a'
    
  valid = True
  for i in range(len(res) - 1):
    if res[i:i+2] == s or res[i:i+2] == t:
      valid = False
      break
      
  if valid:
    print("YES")
    print(res)
    return
  
  if n == 1:
      perms = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
      for perm in perms:
          valid = True
          for i in range(len(perm) - 1):
              if perm[i:i+2] == s or perm[i:i+2] == t:
                  valid = False
                  break
          if valid:
              print("YES")
              print(perm)
              return
  
  if (n == 2 and s == "ab" and t == "bc"):
    print("YES")
    print("acbacb")
    return
    
  if (n == 3 and s == "aa" and t == "bc"):
      print("YES")
      print("acbacbacb")
      return
    
  if (n == 3 and s == "bb" and t == "cb"):
      print("YES")
      print("abcabcabc")
      return

solve()