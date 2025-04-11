def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, left, right, moves):
            nonlocal max_len, best_moves

            if len(current_sequence) > max_len:
                max_len = len(current_sequence)
                best_moves = moves

            if left > right:
                return

            if not current_sequence:
                # Take left
                backtrack(current_sequence + [arr[left]], left + 1, right, moves + "L")
                # Take right
                backtrack(current_sequence + [arr[right]], left, right - 1, moves + "R")
            else:
                last_val = current_sequence[-1]
                
                # Take left
                if arr[left] > last_val:
                    backtrack(current_sequence + [arr[left]], left + 1, right, moves + "L")
                
                # Take right
                if arr[right] > last_val and arr[right] != arr[left]:
                    backtrack(current_sequence + [arr[right]], left, right - 1, moves + "R")
                elif arr[right] > last_val and arr[right] == arr[left]:
                    
                    temp_len_l = 0
                    temp_moves_l = ""
                    temp_len_r = 0
                    temp_moves_r = ""
                    
                    
                    curr_l = left + 1
                    last_val_l = last_val
                    temp_moves_l = "L"
                    temp_len_l = 1
                    
                    while curr_l <= right and arr[curr_l] > last_val_l:
                        last_val_l = arr[curr_l]
                        temp_moves_l += "L"
                        temp_len_l += 1
                        curr_l += 1
                    
                    curr_r = right - 1
                    last_val_r = last_val
                    temp_moves_r = "R"
                    temp_len_r = 1
                    
                    while curr_r >= left and arr[curr_r] > last_val_r:
                        last_val_r = arr[curr_r]
                        temp_moves_r += "R"
                        temp_len_r += 1
                        curr_r -= 1
                    
                    if temp_len_l >= temp_len_r:
                        backtrack(current_sequence + [arr[left]], left + temp_len_l, right, moves + "L" + temp_moves_l[1:])
                    else:
                        backtrack(current_sequence + [arr[right]], left, right - temp_len_r, moves + "R" + temp_moves_r[1:])

        backtrack([], 0, len(a) - 1, "")
        return max_len, best_moves

    length, moves = find_longest_increasing_sequence(a)
    print(length)
    print(moves)

solve()