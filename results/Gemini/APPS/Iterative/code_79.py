def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for suffix in ['00', '25', '50', '75']:
        temp_s = s[:]
        moves = 0

        # Find the last digit of the suffix
        try:
            idx2 = -1
            for i in range(l - 1, -1, -1):
                if temp_s[i] == suffix[1]:
                    idx2 = i
                    break
            if idx2 == -1:
                continue

            # Move the last digit to the end
            for i in range(idx2, l - 1):
                temp_s[i], temp_s[i + 1] = temp_s[i + 1], temp_s[i]
                moves += 1

            # Find the second to last digit of the suffix
            idx1 = -1
            for i in range(l - 2, -1, -1):
                if temp_s[i] == suffix[0]:
                    idx1 = i
                    break
            if idx1 == -1:
                continue

            # Move the second to last digit to the second to last position
            for i in range(idx1, l - 2):
                temp_s[i], temp_s[i + 1] = temp_s[i + 1], temp_s[i]
                moves += 1

            # Remove leading zeros
            first_digit_index = -1
            for i in range(0, l - 2):
                if temp_s[i] != '0':
                    first_digit_index = i
                    break
            
            if first_digit_index == -1:
              if l > 2:
                continue
              else:
                ans = min(ans, moves)
                continue
            
            moves_to_remove_zeros = 0
            for i in range(first_digit_index):
                moves_to_remove_zeros += 1
            
            moves += moves_to_remove_zeros

            ans = min(ans, moves)
        
        except:
            continue

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()