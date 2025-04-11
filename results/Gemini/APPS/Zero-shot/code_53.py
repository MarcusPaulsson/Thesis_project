def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        best_len = 0
        best_moves = ""

        def backtrack(current_seq, remaining_arr, moves):
            nonlocal best_len, best_moves
            
            if not remaining_arr:
                if len(current_seq) > best_len:
                    best_len = len(current_seq)
                    best_moves = moves
                return
            
            if not current_seq or remaining_arr[0] > current_seq[-1]:
                backtrack(current_seq + [remaining_arr[0]], remaining_arr[1:], moves + "L")
            
            if not current_seq or remaining_arr[-1] > current_seq[-1]:
                if len(remaining_arr) > 1 or remaining_arr[0] != remaining_arr[-1]:
                    backtrack(current_seq + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")
            
            if not current_seq and len(remaining_arr) == 1:
                if len(current_seq) + 1 > best_len:
                  best_len = len(current_seq) + 1
                  best_moves = moves + "L"
                return

        backtrack([], a, "")
        return best_len, best_moves

    length, moves = find_longest_increasing_subsequence(a)
    print(length)
    print(moves)

solve()