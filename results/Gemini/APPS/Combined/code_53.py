def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        best_len = 0
        best_moves = ""

        def solve_recursive(current_arr, current_seq, current_moves):
            nonlocal best_len, best_moves

            if len(current_seq) > best_len:
                best_len = len(current_seq)
                best_moves = current_moves

            if not current_arr:
                return

            last_val = current_seq[-1] if current_seq else 0

            if current_arr[0] > last_val and current_arr[-1] > last_val:
                if current_arr[0] < current_arr[-1]:
                    solve_recursive(current_arr[1:], current_seq + [current_arr[0]], current_moves + "L")
                elif current_arr[0] > current_arr[-1]:
                    solve_recursive(current_arr[:-1], current_seq + [current_arr[-1]], current_moves + "R")
                else:
                    left_moves = ""
                    right_moves = ""
                    left_len = 0
                    right_len = 0
                    
                    temp_left_arr = current_arr[:]
                    temp_last_val = last_val
                    
                    temp_right_arr = current_arr[:]
                    
                    
                    
                    
                    
                    
                    
                    temp_left_moves = ""
                    temp_right_moves = ""
                    
                    
                    
                    
                    
                    
                    
                    while temp_left_arr:
                        if temp_left_arr[0] > temp_last_val:
                            temp_last_val = temp_left_arr[0]
                            left_len += 1
                            temp_left_moves += "L"
                            temp_left_arr = temp_left_arr[1:]
                        else:
                            break
                            
                    temp_last_val = last_val
                    
                    while temp_right_arr:
                        if temp_right_arr[-1] > temp_last_val:
                            temp_last_val = temp_right_arr[-1]
                            right_len += 1
                            temp_right_moves += "R"
                            temp_right_arr = temp_right_arr[:-1]
                        else:
                            break

                    if left_len > right_len:
                        solve_recursive(current_arr[1:], current_seq + [current_arr[0]], current_moves + "L")
                    elif right_len > left_len:
                        solve_recursive(current_arr[:-1], current_seq + [current_arr[-1]], current_moves + "R")
                    
                    else:
                         
                        solve_recursive(current_arr[1:], current_seq + [current_arr[0]], current_moves + "L")

            elif current_arr[0] > last_val:
                solve_recursive(current_arr[1:], current_seq + [current_arr[0]], current_moves + "L")
            elif current_arr[-1] > last_val:
                solve_recursive(current_arr[:-1], current_seq + [current_arr[-1]], current_moves + "R")
            else:
                return

        solve_recursive(arr, [], "")
        return best_len, best_moves

    length, moves = find_longest_increasing_sequence(a)
    print(length)
    print(moves)

solve()