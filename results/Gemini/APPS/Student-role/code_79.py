def solve():
    n = input()
    s = list(n)
    length = len(s)
    ans = float('inf')

    for suffix in ["00", "25", "50", "75"]:
        temp_s = s[:]
        moves = 0

        # Find the last digit of the suffix
        try:
            idx2 = -1
            for i in range(length - 1, -1, -1):
                if temp_s[i] == suffix[1]:
                    idx2 = i
                    break
            if idx2 == -1:
                continue

            moves += length - 1 - idx2
            temp_s.pop(idx2)

            # Find the first digit of the suffix
            idx1 = -1
            for i in range(len(temp_s) - 1, -1, -1):
                if temp_s[i] == suffix[0]:
                    idx1 = i
                    break
            if idx1 == -1:
                continue

            moves += len(temp_s) - 1 - idx1
            temp_s.pop(idx1)

            # Remove leading zeroes
            leading_zeroes = 0
            for i in range(len(temp_s)):
                if temp_s[i] == '0':
                    leading_zeroes += 1
                else:
                    break
            
            moves += leading_zeroes
            
            ans = min(ans, moves)
        
        except:
            pass
    
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()