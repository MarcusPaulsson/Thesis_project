def solve():
  n = int(input())
  a = list(map(int, input().split()))

  def find_longest_increasing_sequence(arr):
    max_len = 0
    best_moves = ""

    def backtrack(current_seq, remaining_arr, moves):
      nonlocal max_len, best_moves
      
      if len(current_seq) > max_len:
        max_len = len(current_seq)
        best_moves = moves

      if not remaining_arr:
        return

      last_val = current_seq[-1] if current_seq else -1

      if remaining_arr[0] > last_val:
        backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")

      if len(remaining_arr) > 1 and remaining_arr[-1] > last_val and remaining_arr[0] != remaining_arr[-1]:
          backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
      elif len(remaining_arr) > 1 and remaining_arr[-1] > last_val and remaining_arr[0] == remaining_arr[-1]:
          l_count = 0
          r_count = 0
          temp_arr = remaining_arr[:]
          temp_seq = current_seq[:]
          temp_moves = moves
          max_l = 0
          max_r = 0
          
          
          
          l_seq = current_seq[:]
          l_moves = moves
          l_temp = remaining_arr[:]
          while len(l_temp) > 0 and l_temp[0] > l_seq[-1] if l_seq else True:
              if l_temp[0] > l_seq[-1] if l_seq else True:
                  l_seq.append(l_temp[0])
                  l_moves += "L"
                  l_temp = l_temp[1:]
                  max_l = len(l_seq) - len(current_seq)
              else:
                  break
          
          
          r_seq = current_seq[:]
          r_moves = moves
          r_temp = remaining_arr[:]
          while len(r_temp) > 0 and r_temp[-1] > r_seq[-1] if r_seq else True:
              if r_temp[-1] > r_seq[-1] if r_seq else True:
                  r_seq.append(r_temp[-1])
                  r_moves += "R"
                  r_temp = r_temp[:-1]
                  max_r = len(r_seq) - len(current_seq)
              else:
                  break
          if max_l >= max_r:
              backtrack(l_seq , l_temp, l_moves)
          else:
              backtrack(r_seq , r_temp, r_moves)

      elif len(remaining_arr) == 1 and remaining_arr[0] > last_val:
          backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
          

    backtrack([], arr, "")
    return max_len, best_moves

  max_len, moves = find_longest_increasing_sequence(a)
  print(max_len)
  print(moves)

solve()