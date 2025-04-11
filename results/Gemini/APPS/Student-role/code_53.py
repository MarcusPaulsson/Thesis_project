def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        best_len = 0
        best_seq = ""

        def backtrack(current_seq, current_arr, last_val, moves):
            nonlocal best_len, best_seq

            if not current_arr:
                if len(current_seq) > best_len:
                    best_len = len(current_seq)
                    best_seq = moves
                return

            if current_arr[0] > last_val and current_arr[-1] > last_val:
                if current_arr[0] < current_arr[-1]:
                    backtrack(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                    backtrack(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                elif current_arr[0] > current_arr[-1]:
                    backtrack(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                    backtrack(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                else:
                    
                    temp_arr = current_arr[:]
                    temp_seq = current_seq[:]
                    temp_moves = moves[:]
                    
                    len_l = 0
                    i = 0
                    while i < len(temp_arr) and temp_arr[i] > last_val and temp_arr[i] == temp_arr[0]:
                        len_l += 1
                        i += 1
                    
                    len_r = 0
                    j = len(temp_arr) - 1
                    while j >= 0 and temp_arr[j] > last_val and temp_arr[j] == temp_arr[-1]:
                        len_r += 1
                        j -= 1
                    
                    if len_l > len_r:
                        backtrack(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                    elif len_r > len_l:
                        backtrack(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                    else:
                        
                        
                        temp_arr_l = current_arr[1:]
                        temp_seq_l = current_seq + [current_arr[0]]
                        temp_moves_l = moves + "L"
                        
                        best_len_l = 0
                        best_seq_l = ""
                        
                        def backtrack_l(current_seq, current_arr, last_val, moves):
                            nonlocal best_len_l, best_seq_l
                            
                            if not current_arr:
                                if len(current_seq) > best_len_l:
                                    best_len_l = len(current_seq)
                                    best_seq_l = moves
                                return
                            
                            if current_arr[0] > last_val and current_arr[-1] > last_val:
                                if current_arr[0] < current_arr[-1]:
                                    backtrack_l(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                                    backtrack_l(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                                elif current_arr[0] > current_arr[-1]:
                                    backtrack_l(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                                    backtrack_l(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                                else:
                                    return
                            elif current_arr[0] > last_val:
                                backtrack_l(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                            elif current_arr[-1] > last_val:
                                backtrack_l(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                            else:
                                if len(current_seq) > best_len_l:
                                    best_len_l = len(current_seq)
                                    best_seq_l = moves
                                return
                        
                        backtrack_l(temp_seq_l, temp_arr_l, temp_seq_l[-1], temp_moves_l)
                        
                        
                        temp_arr_r = current_arr[:-1]
                        temp_seq_r = current_seq + [current_arr[-1]]
                        temp_moves_r = moves + "R"
                        
                        best_len_r = 0
                        best_seq_r = ""
                        
                        def backtrack_r(current_seq, current_arr, last_val, moves):
                            nonlocal best_len_r, best_seq_r
                            
                            if not current_arr:
                                if len(current_seq) > best_len_r:
                                    best_len_r = len(current_seq)
                                    best_seq_r = moves
                                return
                            
                            if current_arr[0] > last_val and current_arr[-1] > last_val:
                                if current_arr[0] < current_arr[-1]:
                                    backtrack_r(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                                    backtrack_r(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                                elif current_arr[0] > current_arr[-1]:
                                    backtrack_r(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                                    backtrack_r(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                                else:
                                    return
                            elif current_arr[0] > last_val:
                                backtrack_r(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
                            elif current_arr[-1] > last_val:
                                backtrack_r(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
                            else:
                                if len(current_seq) > best_len_r:
                                    best_len_r = len(current_seq)
                                    best_seq_r = moves
                                return
                        
                        backtrack_r(temp_seq_r, temp_arr_r, temp_seq_r[-1], temp_moves_r)
                        
                        if best_len_l > best_len_r:
                            if len(temp_seq_l) + best_len_l - len(temp_seq_l) > best_len:
                                best_len = len(temp_seq_l) + best_len_l - len(temp_seq_l)
                                best_seq = temp_moves_l + best_seq_l
                        elif best_len_r > best_len_l:
                            if len(temp_seq_r) + best_len_r - len(temp_seq_r) > best_len:
                                best_len = len(temp_seq_r) + best_len_r - len(temp_seq_r)
                                best_seq = temp_moves_r + best_seq_r
                        else:
                            if len(temp_seq_l) + best_len_l - len(temp_seq_l) > best_len:
                                best_len = len(temp_seq_l) + best_len_l - len(temp_seq_l)
                                best_seq = temp_moves_l + best_seq_l
                            
                        return
                            
            elif current_arr[0] > last_val:
                backtrack(current_seq + [current_arr[0]], current_arr[1:], current_arr[0], moves + "L")
            elif current_arr[-1] > last_val:
                backtrack(current_seq + [current_arr[-1]], current_arr[:-1], current_arr[-1], moves + "R")
            else:
                if len(current_seq) > best_len:
                    best_len = len(current_seq)
                    best_seq = moves
                return

        backtrack([], arr, 0, "")
        return best_len, best_seq

    length, sequence = find_longest_increasing_subsequence(a)
    print(length)
    print(sequence)

solve()