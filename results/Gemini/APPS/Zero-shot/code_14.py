def solve():
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  
  used = set(p)
  remaining = []
  for i in range(n, 0, -1):
    if i not in used:
      remaining.append(i)
  
  p += remaining
  
  def is_stack_sortable(arr):
    a = arr[:]
    s = []
    b = []
    
    i = 0
    while i < 2 * n:
      if len(a) > 0 and (len(s) == 0 or a[0] < s[-1]):
        s.append(a[0])
        a.pop(0)
        i += 1
      elif len(s) > 0:
        b.append(s[-1])
        s.pop()
        i += 1
      else:
        return False
    
    for i in range(len(b) - 1):
      if b[i] > b[i+1]:
        return False
    return True

  
  def find_lexicographically_maximal(arr):
      
    used_init = set(arr[:k])
    remaining_init = []
    for i in range(n, 0, -1):
        if i not in used_init:
            remaining_init.append(i)

    
    import itertools
    
    best_arr = None

    for perm in itertools.permutations(remaining_init):
        curr_arr = arr[:k] + list(perm)
        if is_stack_sortable(curr_arr):
            if best_arr is None:
                best_arr = curr_arr
            else:
                if curr_arr > best_arr:
                    best_arr = curr_arr

    return best_arr
  
  
  result = find_lexicographically_maximal(p[:])
  if result is None:
    print(-1)
  else:
    print(*result)

solve()