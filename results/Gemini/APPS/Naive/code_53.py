def solve():
  n = int(input())
  a = list(map(int, input().split()))
  
  def find_longest_increasing_sequence(arr):
    max_len = 0
    best_moves = ""
    
    def backtrack(current_seq, remaining_arr, moves):
      nonlocal max_len, best_moves
      
      if not remaining_arr:
        if len(current_seq) > max_len:
          max_len = len(current_seq)
          best_moves = moves
        return
      
      if not current_seq:
        # Take left
        backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
        # Take right
        backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
      else:
        last_val = current_seq[-1]
        
        # Take left
        if remaining_arr[0] > last_val:
          backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
        
        # Take right
        if remaining_arr[-1] > last_val:
          backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
    
    backtrack([], arr, "")
    return max_len, best_moves
  
  len_seq, moves = find_longest_increasing_sequence(a)
  print(len_seq)
  print(moves)

solve()