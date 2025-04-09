def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    used = [False] * (n + 1)
    for x in p:
        used[x] = True

    remaining = []
    for i in range(n, 0, -1):
        if not used[i]:
            remaining.append(i)

    p_full = p[:]
    for x in remaining:
        p_full.append(x)

    def is_stack_sortable(arr):
        s = []
        b = []
        a = arr[:]
        
        i = 0
        while i < 2 * n:
            if len(a) > 0 and (len(s) == 0 or a[0] < s[-1]):
                s.append(a[0])
                a.pop(0)
            elif len(s) > 0:
                b.append(s[-1])
                s.pop()
            else:
                return False
            i += 1

        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    if not is_stack_sortable(p_full):
        print("-1")
        return

    
    remaining = []
    for i in range(n, 0, -1):
        if not used[i]:
            remaining.append(i)
    
    p_full = p[:]
    
    def find_lexicographically_largest(current_permutation, remaining_numbers):
      if len(current_permutation) == n:
        if is_stack_sortable(current_permutation):
          return current_permutation
        else:
          return None
      
      best_permutation = None
      for i in range(len(remaining_numbers) - 1, -1, -1):
        new_permutation = current_permutation + [remaining_numbers[i]]
        new_remaining = remaining_numbers[:i] + remaining_numbers[i+1:]
        
        
        potential_permutation = find_lexicographically_largest(new_permutation, new_remaining)
        
        if potential_permutation is not None:
          if best_permutation is None or potential_permutation > best_permutation:
            best_permutation = potential_permutation
      return best_permutation
    
    result = find_lexicographically_largest(p, remaining)
    
    if result is None:
      print("-1")
    else:
      print(*result)

solve()