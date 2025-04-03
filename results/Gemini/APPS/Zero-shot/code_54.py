def solve():
  n = int(input())
  a = list(map(int, input().split()))

  unique_vals = sorted(list(set(a)))

  if len(unique_vals) > 3:
    print("-1")
    return
  
  if len(unique_vals) == 1:
    print("0")
    return
  
  if len(unique_vals) == 2:
    val1, val2 = unique_vals
    diff = abs(val1 - val2)
    if diff % 2 == 0:
      print(diff // 2)
    else:
      print(diff)
    return

  if len(unique_vals) == 3:
    val1, val2, val3 = unique_vals
    if val2 - val1 == val3 - val2:
      print(val2 - val1)
    else:
      print("-1")
    return
    

solve()