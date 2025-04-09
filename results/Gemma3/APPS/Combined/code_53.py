def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def get_longest_increasing_sequence(arr):
        max_len = 0
        best_moves = ""
        
        def backtrack(current_seq, moves, current_arr):
            nonlocal max_len, best_moves
            
            if len(current_seq) > max_len:
                max_len = len(current_seq)
                best_moves = moves
            
            if not current_arr:
                return
            
            # Take leftmost
            if not current_seq or current_arr[0] > current_seq[-1]:
                backtrack(current_seq + [current_arr[0]], moves + "L", current_arr[1:])
            
            # Take rightmost
            if not current_seq or current_arr[-1] > current_seq[-1]:
                backtrack(current_seq + [current_arr[-1]], moves + "R", current_arr[:-1])
        
        backtrack([], "", arr)
        return max_len, best_moves
    
    max_len, best_moves = get_longest_increasing_sequence(a)
    
    print(max_len)
    print(best_moves)

solve()