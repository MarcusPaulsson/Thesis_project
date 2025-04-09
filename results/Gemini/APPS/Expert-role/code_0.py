def solve():
  s = input()
  n = len(s)
  
  max_len = -1
  
  for i in range(n):
    if s[i] == '[':
      for j in range(n - 1, i, -1):
        if s[j] == ']':
          
          first_colon_index = -1
          for k in range(i + 1, j):
            if s[k] == ':':
              first_colon_index = k
              break
          
          if first_colon_index == -1:
            continue
            
          second_colon_index = -1
          for k in range(j - 1, first_colon_index, -1):
            if s[k] == ':':
              second_colon_index = k
              break
              
          if second_colon_index == -1:
            continue
          
          
          vertical_bars_count = 0
          for k in range(first_colon_index + 1, second_colon_index):
            if s[k] == '|':
              vertical_bars_count += 1
              
          current_len = 2 + 2 + vertical_bars_count
          max_len = max(max_len, current_len)
            
  print(max_len)
  
solve()