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
                # Choose left
                backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                # Choose right
                backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
            else:
                last_val = current_seq[-1]
                
                # Choose left
                if remaining_arr[0] > last_val:
                    backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                
                # Choose right
                if remaining_arr[-1] > last_val:
                    backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")

        backtrack([], a, "")
        return max_len, best_moves

    def find_longest_increasing_sequence_optimized(arr):
        n = len(arr)
        max_len = 0
        best_moves = ""

        def solve_recursive(left, right, last, moves):
            nonlocal max_len, best_moves

            if left > right:
                if len(moves) > max_len:
                    max_len = len(moves)
                    best_moves = moves
                return

            if arr[left] > last and arr[right] > last:
                if arr[left] < arr[right]:
                    solve_recursive(left + 1, right, arr[left], moves + "L")
                elif arr[left] > arr[right]:
                    solve_recursive(left, right - 1, arr[right], moves + "R")
                else:
                    len_left = 0
                    len_right = 0
                    
                    temp_left = left + 1
                    while temp_left <= right and arr[temp_left] > arr[left]:
                        len_left += 1
                        temp_left += 1
                    
                    temp_right = right - 1
                    while temp_right >= left and arr[temp_right] > arr[right]:
                        len_right += 1
                        temp_right -= 1

                    if len_left > len_right:
                        solve_recursive(left + 1, right, arr[left], moves + "L")
                    else:
                        solve_recursive(left, right - 1, arr[right], moves + "R")

            elif arr[left] > last:
                solve_recursive(left + 1, right, arr[left], moves + "L")

            elif arr[right] > last:
                solve_recursive(left, right - 1, arr[right], moves + "R")
            
            else:
                if len(moves) > max_len:
                    max_len = len(moves)
                    best_moves = moves
                return

        solve_recursive(0, n - 1, 0, "")
        return max_len, best_moves
    
    length, moves = find_longest_increasing_sequence_optimized(a)
    print(length)
    print(moves)

solve()