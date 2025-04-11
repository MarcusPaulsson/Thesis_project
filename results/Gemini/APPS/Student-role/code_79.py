def solve():
    n = input()
    n_list = list(n)
    n_len = len(n)
    
    def calculate_moves(arr):
        moves = 0
        for i in range(len(arr)):
            if arr[i] != i:
                j = arr.index(i)
                moves += j - i
                arr = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
        return moves

    def check_leading_zeros(s):
        return len(s) == 1 or s[0] != '0'

    def find_min_moves(digits):
        min_moves = float('inf')
        
        import itertools
        
        for p in itertools.permutations(digits):
            s = "".join(p)
            if check_leading_zeros(s) and int(s) % 25 == 0:
                
                arr = list(range(len(digits)))
                digit_indices = {}
                for i in range(len(digits)):
                    if digits[i] not in digit_indices:
                        digit_indices[digits[i]] = []
                    digit_indices[digits[i]].append(i)
                
                permutation_indices = []
                for digit in p:
                    permutation_indices.append(digit_indices[digit].pop(0))
                
                moves = calculate_moves(arr)
                min_moves = min(min_moves, moves)
        
        if min_moves == float('inf'):
            return -1
        else:
            return min_moves

    min_moves = float('inf')
    
    for i in range(n_len):
        for j in range(i + 1, n_len):
            if (int(n_list[i]) * 10 + int(n_list[j])) % 25 == 0:
                
                temp_list = n_list[:]
                
                moves = 0
                
                moves += (n_len - 1) - j
                temp_list.insert(n_len, temp_list.pop(j))
                
                moves += (n_len - 1) - i
                temp_list.insert(n_len, temp_list.pop(i))
                
                first_non_zero = -1
                for k in range(n_len - 2):
                    if temp_list[k] != '0':
                        first_non_zero = k
                        break
                
                if first_non_zero == -1:
                    if n_len - 2 > 0:
                        continue
                else:
                    moves += first_non_zero
                    temp_list.insert(0, temp_list.pop(first_non_zero))
                
                min_moves = min(min_moves, moves)

    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)

solve()