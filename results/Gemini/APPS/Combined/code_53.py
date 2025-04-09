def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        n = len(arr)
        dp = {}

        def solve_dp(left, right, last):
            if (left, right, last) in dp:
                return dp[(left, right, last)]

            if left > right:
                return 0, ""

            ans1 = 0
            moves1 = ""
            if arr[left] > last:
                len1, moves_str1 = solve_dp(left + 1, right, arr[left])
                ans1 = 1 + len1
                moves1 = "L" + moves_str1

            ans2 = 0
            moves2 = ""
            if arr[right] > last:
                len2, moves_str2 = solve_dp(left, right - 1, arr[right])
                ans2 = 1 + len2
                moves2 = "R" + moves_str2

            if ans1 > ans2:
                dp[(left, right, last)] = ans1, moves1
            elif ans2 > ans1:
                dp[(left, right, last)] = ans2, moves2
            else:
                if ans1 == 0:
                    dp[(left, right, last)] = 0, ""
                else:
                    dp[(left, right, last)] = ans1, (moves1 if moves1 < moves2 else moves2)
            
            return dp[(left, right, last)]
        
        length, moves = solve_dp(0, n - 1, 0)
        return length, moves

    length, moves = find_longest_increasing_subsequence(a)
    print(length)
    print(moves)

solve()