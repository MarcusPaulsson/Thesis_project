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
            idx1 = -1
            for i in range(l - 1, -1, -1):
                if temp_s[i] == suffix[1]:
                    idx1 = i
                    break
            if idx1 == -1:
                continue

            moves += (l - 1 - idx1)
            del temp_s[idx1]

            # Find the second last digit of the suffix
            idx2 = -1
            for i in range(len(temp_s) - 1, -1, -1):
                if temp_s[i] == suffix[0]:
                    idx2 = i
                    break

            if idx2 == -1:
                continue

            moves += (len(temp_s) - 1 - idx2)
            del temp_s[idx2]
            
            # Remove leading zeros
            leading_zeros = 0
            for i in range(len(temp_s)):
                if temp_s[i] == '0':
                    leading_zeros += 1
                else:
                    break
            
            moves += leading_zeros

            ans = min(ans, moves)

        except ValueError:
            continue
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()