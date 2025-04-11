def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for i in range(l):
        for j in range(i + 1, l):
            if (s[i] == '0' and s[j] == '0') or (s[i] == '2' and s[j] == '5') or (s[i] == '5' and s[j] == '0') or (s[i] == '7' and s[j] == '5') or (s[i] == '0' and s[j] == '5') or (s[i] == '5' and s[j] == '0'):
                temp = s[:]
                moves = 0

                # Move the second digit to the last position
                for k in range(j, l - 1):
                    temp[k], temp[k + 1] = temp[k + 1], temp[k]
                    moves += 1

                # Move the first digit to the second last position
                for k in range(i, l - 2):
                    temp[k], temp[k + 1] = temp[k + 1], temp[k]
                    moves += 1

                # Remove leading zeros
                leading_zeros = 0
                for k in range(l - 2):
                    if temp[k] == '0':
                        leading_zeros += 1
                    else:
                        break

                # If there are leading zeroes after removing the last 2 digits
                if leading_zeros > 0:
                    # Swap the first non-zero digit with the leading zero(s)
                    first_non_zero_idx = -1
                    for k in range(leading_zeros, l - 2):
                        if temp[k] != '0':
                            first_non_zero_idx = k
                            break

                    if first_non_zero_idx != -1:
                        for k in range(first_non_zero_idx, leading_zeros, -1):
                            temp[k], temp[k - 1] = temp[k - 1], temp[k]
                            moves += 1
                    else:
                        continue
                
                ans = min(ans, moves)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()