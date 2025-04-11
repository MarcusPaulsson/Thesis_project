def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, remaining_arr, moves):
            nonlocal max_len, best_moves

            if not remaining_arr:
                if len(current_sequence) > max_len:
                    max_len = len(current_sequence)
                    best_moves = moves
                return

            if not current_sequence:
                # Take left
                backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                # Take right
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
            else:
                last_val = current_sequence[-1]
                
                # Take left
                if remaining_arr[0] > last_val:
                    backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")
                
                # Take right
                if remaining_arr[-1] > last_val:
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
                elif arr[right] < arr[left]:
                    solve_recursive(left, right - 1, arr[right], moves + "R")
                else:
                    len_left, moves_left = solve_helper(left + 1, right, arr[left], "L")
                    len_right, moves_right = solve_helper(left, right - 1, arr[right], "R")

                    if len_left > len_right:
                        solve_recursive(left + 1, right, arr[left], moves + "L")
                    elif len_right > len_left:
                        solve_recursive(left, right - 1, arr[right], moves + "R")
                    else:
                        solve_recursive(left + 1, right, arr[left], moves + "L")
            elif arr[left] > last_val:
                solve_recursive(left + 1, right, arr[left], moves + "L")
            elif arr[right] > last_val:
                solve_recursive(left, right - 1, arr[right], moves + "R")
            else:
                if len(moves) > max_len:
                    max_len = len(moves)
                    best_moves = moves
                return

        def solve_helper(left, right, last_val, moves):
            curr_len = 0
            curr_moves = ""
            while left <= right:
                if arr[left] > last_val and arr[right] > last_val:
                    if arr[left] < arr[right]:
                        last_val = arr[left]
                        curr_moves += "L"
                        left += 1
                    elif arr[right] < arr[left]:
                        last_val = arr[right]
                        curr_moves += "R"
                        right -= 1
                    else:
                        len_left, moves_left = solve_helper(left + 1, right, arr[left], "L")
                        len_right, moves_right = solve_helper(left, right - 1, arr[right], "R")
                        
                        if len_left > len_right:
                            last_val = arr[left]
                            curr_moves += "L"
                            left += 1
                        else:
                            last_val = arr[right]
                            curr_moves += "R"
                            right -= 1
                        break
                elif arr[left] > last_val:
                    last_val = arr[left]
                    curr_moves += "L"
                    left += 1
                elif arr[right] > last_val:
                    last_val = arr[right]
                    curr_moves += "R"
                    right -= 1
                else:
                    break
            return len(curr_moves), moves + curr_moves

        solve_recursive(0, n - 1, 0, "")
        return max_len, best_moves

    length, moves = find_longest_increasing_sequence_optimized(a)
    print(length)
    print(moves)

solve()