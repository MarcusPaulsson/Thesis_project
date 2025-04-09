def solve():
  n = int(input())
  a = input()
  f = list(map(int, input().split()))

  best_a = a
  
  for i in range(n):
    for j in range(i, n):
      temp_a_list = list(a)
      for k in range(i, j + 1):
        digit = int(a[k])
        temp_a_list[k] = str(f[digit - 1])
      
      temp_a = "".join(temp_a_list)
      if temp_a > best_a:
        best_a = temp_a
        
  print(best_a)

solve()