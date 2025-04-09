def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def find_longest_increasing_subsequence(arr):
        q = [(arr, [], -1, "")]
        max_len = 0
        best_path = ""

        while q:
            curr_arr, curr_seq, last_val, curr_path = q.pop(0)

            if not curr_arr:
                if len(curr_seq) > max_len:
                    max_len = len(curr_seq)
                    best_path = curr_path
                continue

            left_val = curr_arr[0]
            right_val = curr_arr[-1]

            if left_val > last_val:
                q.append((curr_arr[1:], curr_seq + [left_val], left_val, curr_path + "L"))

            if len(curr_arr) > 1 and right_val > last_val:
                q.append((curr_arr[:-1], curr_seq + [right_val], right_val, curr_path + "R"))
            elif len(curr_arr) == 1 and right_val > last_val:
                if len(curr_seq) + 1 > max_len:
                     max_len = len(curr_seq) + 1
                     best_path = curr_path + 'R'
                     
        return max_len, best_path

    max_len, best_path = find_longest_increasing_subsequence(a)
    print(max_len)
    print(best_path)

solve()