def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        max_len = 0
        best_moves = ""

        def backtrack(current_sequence, remaining_arr, moves):
            nonlocal max_len, best_moves
            
            if not remaining_arr:
                if len(current_sequence) > max_len:
                    max_len = len(current_sequence)
                    best_moves = moves
                return

            if not current_sequence or remaining_arr[0] > current_sequence[-1]:
                backtrack(current_sequence + [remaining_arr[0]], remaining_arr[1:], moves + "L")

            if not current_sequence or remaining_arr[-1] > current_sequence[-1]:
                backtrack(current_sequence + [remaining_arr[-1]], remaining_arr[:-1], moves + "R")

        backtrack([], a, "")

        return max_len, best_moves

    length, moves = find_longest_increasing_subsequence(a)
    print(length)
    print(moves)

solve()