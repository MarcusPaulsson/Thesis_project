def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
        best_len = 0
        best_moves = ""

        def backtrack(current_seq, remaining_arr, moves):
            nonlocal best_len, best_moves

            if not remaining_arr:
                if len(current_seq) > best_len:
                    best_len = len(current_seq)
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
        return best_len, best_moves

    def find_longest_increasing_sequence_dp(arr):
        n = len(arr)
        max_len = 0
        best_moves = ""

        for i in range(1 << n):
            
            moves = ""
            temp_arr = arr[:]
            current_seq = []
            idx = 0
            possible = True

            for j in range(n):
                if (i >> j) & 1:
                    if not temp_arr:
                        possible = False
                        break
                    if not current_seq:
                        current_seq.append(temp_arr.pop(0))
                        moves += "L"
                    elif temp_arr[0] > current_seq[-1]:
                        current_seq.append(temp_arr.pop(0))
                        moves += "L"
                    else:
                        possible = False
                        break
                else:
                    if not temp_arr:
                        possible = False
                        break
                    if not current_seq:
                        current_seq.append(temp_arr.pop())
                        moves += "R"
                    elif temp_arr[-1] > current_seq[-1]:
                        current_seq.append(temp_arr.pop())
                        moves += "R"
                    else:
                        possible = False
                        break

            if possible and len(current_seq) > max_len:
                max_len = len(current_seq)
                best_moves = moves

        return max_len, best_moves

    def solve_optimized(arr):
        n = len(arr)
        
        def get_max_len(left, right, last_val, moves):
            if left > right:
                return len(moves), moves

            len_left = 0
            moves_left = ""
            
            if arr[left] > last_val:
                len_left, moves_left = get_max_len(left + 1, right, arr[left], moves + "L")

            len_right = 0
            moves_right = ""

            if arr[right] > last_val:
                len_right, moves_right = get_max_len(left, right - 1, arr[right], moves + "R")

            if len_left >= len_right:
                return len_left, moves_left
            else:
                return len_right, moves_right

        length, moves = get_max_len(0, n - 1, -1, "")
        return length, moves

    length, moves = solve_optimized(a)
    print(length)
    print(moves)

solve()