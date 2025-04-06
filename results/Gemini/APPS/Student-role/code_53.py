def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        best_len = 0
        best_seq = ""

        def backtrack(current_seq, current_arr, last_val, moves):
            nonlocal best_len, best_seq
            
            if not current_arr:
                if len(current_seq) > best_len:
                    best_len = len(current_seq)
                    best_seq = moves
                return
            
            if current_arr[0] > last_val:
                backtrack(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
            
            if len(current_arr) > 1 and current_arr[-1] > last_val:
                backtrack(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
            
            if len(current_seq) > best_len:
                best_len = len(current_seq)
                best_seq = moves

        backtrack([], a, 0, "")
        return best_len, best_seq
    
    
    def find_longest_increasing_sequence_dp(arr):
      n = len(arr)
      
      max_len = 0
      best_moves = ""

      def solve_recursive(left, right, last_val, current_len, current_moves):
          nonlocal max_len, best_moves

          if left > right:
              if current_len > max_len:
                  max_len = current_len
                  best_moves = current_moves
              return
          
          if arr[left] > last_val and arr[right] > last_val:
              if arr[left] < arr[right]:
                  solve_recursive(left + 1, right, arr[left], current_len + 1, current_moves + "L")
                  solve_recursive(left, right - 1, arr[right], current_len + 1, current_moves + "R")
              elif arr[left] > arr[right]:
                  solve_recursive(left, right - 1, arr[right], current_len + 1, current_moves + "R")
                  solve_recursive(left + 1, right, arr[left], current_len + 1, current_moves + "L")
              else:
                  len_l, moves_l = find_max_len_from_left(left+1, right, arr[left])
                  len_r, moves_r = find_max_len_from_right(left, right-1, arr[right])

                  if len_l >= len_r:
                      solve_recursive(left + 1, right, arr[left], current_len + 1 + len_l, current_moves + "L" + moves_l)
                  else:
                      solve_recursive(left, right - 1, arr[right], current_len + 1 + len_r, current_moves + "R" + moves_r)
          elif arr[left] > last_val:
              solve_recursive(left + 1, right, arr[left], current_len + 1, current_moves + "L")
          elif arr[right] > last_val:
              solve_recursive(left, right - 1, arr[right], current_len + 1, current_moves + "R")
          else:
              if current_len > max_len:
                  max_len = current_len
                  best_moves = current_moves
              return
      
      def find_max_len_from_left(left, right, last_val):
          len_l = 0
          moves_l = ""
          while left <= right and arr[left] > last_val:
              len_l += 1
              moves_l += "L"
              last_val = arr[left]
              left += 1
          return len_l, moves_l

      def find_max_len_from_right(left, right, last_val):
          len_r = 0
          moves_r = ""
          while left <= right and arr[right] > last_val:
              len_r += 1
              moves_r += "R"
              last_val = arr[right]
              right -= 1
          return len_r, moves_r
      
      solve_recursive(0, n-1, 0, 0, "")
      return max_len, best_moves

    length, sequence = find_longest_increasing_sequence_dp(a)
    print(length)
    print(sequence)

solve()