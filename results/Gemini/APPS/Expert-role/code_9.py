def solve():
  d = int(input())
  n, m = map(int, input().split())
  sofas = []
  for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))
  cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
  
  def is_left(sofa1, sofa2):
    x11, y11, x12, y12 = sofa1
    x21, y21, x22, y22 = sofa2
    
    return min(y11, y12) < max(y21, y22)

  def is_right(sofa1, sofa2):
    x11, y11, x12, y12 = sofa1
    x21, y21, x22, y22 = sofa2
    
    return max(y11, y12) > min(y21, y22)

  def is_top(sofa1, sofa2):
    x11, y11, x12, y12 = sofa1
    x21, y21, x22, y22 = sofa2
    
    return min(x11, x12) < max(x21, x22)

  def is_bottom(sofa1, sofa2):
    x11, y11, x12, y12 = sofa1
    x21, y21, x22, y22 = sofa2
    
    return max(x11, x12) > min(x21, x22)
  
  
  for i in range(d):
    l_count = 0
    r_count = 0
    t_count = 0
    b_count = 0
    
    for j in range(d):
      if i != j:
        if is_left(sofas[i], sofas[j]):
          l_count += 1
        if is_right(sofas[i], sofas[j]):
          r_count += 1
        if is_top(sofas[i], sofas[j]):
          t_count += 1
        if is_bottom(sofas[i], sofas[j]):
          b_count += 1
    
    if l_count == cnt_l and r_count == cnt_r and t_count == cnt_t and b_count == cnt_b:
      print(i + 1)
      return
  
  print(-1)

solve()