def solve():
  n = int(input())
  s = input()

  for i in range(1 << n):
    coloring = ""
    s1 = ""
    s2 = ""
    for j in range(n):
      if (i >> j) & 1:
        coloring += "1"
        s2 += s[j]
      else:
        coloring += "0"
        s1 += s[j]

    s1_sorted = "".join(sorted(s1))
    s2_sorted = "".join(sorted(s2))

    merged = ""
    i1 = 0
    i2 = 0
    
    possible = True
    
    for k in range(n):
      if coloring[k] == '0':
        if i1 < len(s1_sorted):
          merged += s1_sorted[i1]
          i1 += 1
        else:
          possible = False
          break
          
      else:
        if i2 < len(s2_sorted):
          merged += s2_sorted[i2]
          i2 += 1
        else:
          possible = False
          break
    
    if not possible:
        continue
    
    
    
    if "".join(sorted(s)) == merged:
      print("YES")
      print(coloring)
      return

  print("NO")

solve()