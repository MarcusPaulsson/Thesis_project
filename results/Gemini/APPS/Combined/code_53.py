def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_sequence(arr):
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
                    solve_recursive(left, right - 1, arr[right], moves + "R")
                elif arr[left] > arr[right]:
                    solve_recursive(left, right - 1, arr[right], moves + "R")
                    solve_recursive(left + 1, right, arr[left], moves + "L")
                else:
                    temp_left = ""
                    temp_right = ""
                    l = left
                    r = right
                    while l <= r and arr[l] > last_val and arr[l] == arr[left]:
                        temp_left += "L"
                        l += 1
                    
                    l = left
                    r = right
                    while l <= r and arr[r] > last_val and arr[r] == arr[right]:
                        temp_right += "R"
                        r -= 1
                    
                    if len(temp_left) > len(temp_right):
                        solve_recursive(left + len(temp_left), right, arr[left], moves + temp_left)
                    elif len(temp_right) > len(temp_left):
                        solve_recursive(left, right - len(temp_right), arr[right], moves + temp_right)
                    else:
                        if moves + temp_left < moves + temp_right:
                            solve_recursive(left + len(temp_left), right, arr[left], moves + temp_left)
                        else:
                            solve_recursive(left, right - len(temp_right), arr[right], moves + temp_right)
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

    max_len, best_moves = find_longest_increasing_sequence(a)
    print(max_len)
    print(best_moves)

solve()