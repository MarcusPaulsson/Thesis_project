def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    if any(counts[x] > k for x in counts):
        print("NO")
        return

    print("YES")
    colors = [0] * n
    color_assignment = {}
    color_idx = 1

    for i in range(n):
        num = a[i]
        if num not in color_assignment:
            color_assignment[num] = []
        
        if len(color_assignment[num]) < k:
            colors[i] = len(color_assignment[num]) + 1
            color_assignment[num].append(i)
        

    used_colors = set()
    
    for i in range(n):
       used_colors.add(colors[i])
   
    
    if len(used_colors) < k:
      indices_to_recolor = []
      for i in range(n):
          if colors[i] == 0:
              indices_to_recolor.append(i)

      
      available_colors = set(range(1,k+1))
      for color in used_colors:
          if color in available_colors:
              available_colors.remove(color)
      
      available_colors = list(available_colors)
      
      
      for i in indices_to_recolor:
        if len(available_colors) > 0 :
          colors[i] = available_colors[0]
          available_colors.pop(0)
        else:
          colors[i] = 1
          
          
    
    
    used_colors = set()
    for i in range(n):
        used_colors.add(colors[i])

    
    if len(used_colors) < k:
        
      
        empty_color_indices = []

        for i in range(1, k+1):
            found = False
            for j in range(n):
                if colors[j] == i:
                    found = True
                    break
            if not found:
                empty_color_indices.append(i)
        
        
        if len(empty_color_indices) > 0:
          print("NO")
          return

    print(*colors)

solve()