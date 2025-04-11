def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, remaining_arr, moves):
            nonlocal max_len, best_moves

            if len(current_sequence) > max_len:
                max_len = len(current_sequence)
                best_moves = moves

            if not remaining_arr:
                return

            if not current_sequence:
                # Take left
                backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                # Take right
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
            else:
                last_element = current_sequence[-1]
                
                # Take left
                if remaining_arr[0] > last_element:
                    backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                # Take right
                if remaining_arr[-1] > last_element:
                    backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")

        backtrack([], a, "")
        return max_len, best_moves

    def find_longest_increasing_sequence_optimized(arr):
        n = len(arr)
        max_len = 0
        best_moves = ""

        def solve_recursive(left, right, last_val, moves):
            nonlocal max_len, best_moves

            if left > right:
                if len(moves) > max_len:
                    max_len = len(moves)
                    best_moves = moves
                return

            if arr[left] > last_val and arr[right] > last_val:
                if arr[left] < arr[right]:
                    solve_recursive(left + 1, right, arr[left], moves + "L")
                    if len(moves) + 1 > max_len:
                        solve_recursive(left, right - 1, arr[right], moves + "R")
                elif arr[left] > arr[right]:
                    solve_recursive(left, right - 1, arr[right], moves + "R")
                    if len(moves) + 1 > max_len:
                        solve_recursive(left + 1, right, arr[left], moves + "L")
                else:
                    len_left = 0
                    temp_left = left
                    last_left = arr[left]
                    while temp_left <= right and arr[temp_left] > last_left:
                        len_left += 1
                        last_left = arr[temp_left]
                        temp_left += 1

                    len_right = 0
                    temp_right = right
                    last_right = arr[right]
                    while temp_right >= left and arr[temp_right] > last_right:
                        len_right += 1
                        last_right = arr[temp_right]
                        temp_right -= 1
                    
                    if len_left > len_right:
                        solve_recursive(left + len_left, right, arr[left + len_left -1], moves + "L" * len_left)
                    else:
                        solve_recursive(left, right - len_right, arr[right - len_right + 1], moves + "R" * len_right)
            elif arr[left] > last_val:
                solve_recursive(left + 1, right, arr[left], moves + "L")
            elif arr[right] > last_val:
                solve_recursive(left, right - 1, arr[right], moves + "R")
            else:
                if len(moves) > max_len:
                    max_len = len(moves)
                    best_moves = moves
                return

        solve_recursive(0, n - 1, 0, "")
        return max_len, best_moves
    
    
    def find_longest_increasing_sequence_iterative(arr):
        n = len(arr)
        
        max_len = 0
        best_moves = ""
        
        for start_side in ['L', 'R']:
            
            q = [(0, n - 1, 0, "", -1)] # (left, right, last_val, moves, last_side)
            
            while q:
                left, right, last_val, moves, last_side = q.pop(0)
                
                if left > right:
                    if len(moves) > max_len:
                        max_len = len(moves)
                        best_moves = moves
                    continue
                
                
                if arr[left] > last_val and arr[right] > last_val:
                    if arr[left] < arr[right]:
                        q.append((left + 1, right, arr[left], moves + "L", 0))
                        q.append((left, right - 1, arr[right], moves + "R", 1))
                    elif arr[left] > arr[right]:
                        q.append((left, right - 1, arr[right], moves + "R", 1))
                        q.append((left + 1, right, arr[left], moves + "L", 0))
                    else:
                        len_left = 0
                        temp_left = left
                        last_left = arr[left]
                        while temp_left <= right and arr[temp_left] > last_left:
                            len_left += 1
                            last_left = arr[temp_left]
                            temp_left += 1

                        len_right = 0
                        temp_right = right
                        last_right = arr[right]
                        while temp_right >= left and arr[temp_right] > last_right:
                            len_right += 1
                            last_right = arr[temp_right]
                            temp_right -= 1
                        
                        if len_left > len_right:
                            q.append((left + len_left, right, arr[left + len_left -1], moves + "L" * len_left, 0))
                        else:
                            q.append((left, right - len_right, arr[right - len_right + 1], moves + "R" * len_right, 1))
                elif arr[left] > last_val:
                    q.append((left + 1, right, arr[left], moves + "L", 0))
                elif arr[right] > last_val:
                    q.append((left, right - 1, arr[right], moves + "R", 1))
                else:
                    if len(moves) > max_len:
                        max_len = len(moves)
                        best_moves = moves
                    continue
        
        return max_len, best_moves
    
    
    
    length, moves = find_longest_increasing_sequence_optimized(a)
    print(length)
    print(moves)

solve()