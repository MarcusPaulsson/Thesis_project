def solve():
  n = int(input())
  s = input()
  
  colors = [0] * n
  
  def check(num_colors):
    
    def is_sortable(arr, color_assignment):
      
      def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
      
      arr_copy = list(arr)
      color_assignment_copy = list(color_assignment)
      
      
      for _ in range(n * (n - 1) // 2):
        swapped = False
        for i in range(n - 1):
          if arr_copy[i] > arr_copy[i+1] and color_assignment_copy[i] != color_assignment_copy[i+1]:
            swap(arr_copy, i, i+1)
            swap(color_assignment_copy, i, i+1)
            swapped = True
        if not swapped:
          break
      
      return arr_copy == sorted(arr)

    
    import itertools
    
    for color_assignment in itertools.product(range(1, num_colors + 1), repeat=n):
      if is_sortable(list(s), list(color_assignment)):
          return True, list(color_assignment)
    return False, None
  
  for num_colors in range(1, n + 1):
    possible, assignment = check(num_colors)
    if possible:
      print(num_colors)
      print(*assignment)
      return

solve()