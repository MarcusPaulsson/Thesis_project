def solve():
    n = input()
    n_len = len(n)
    
    def calculate_moves(s):
        moves = 0
        
        # Move the last digit to the end
        for i in range(len(s) - 1, 0, -1):
            if s[i] == s[-1]:
                moves += len(s) - 1 - i
                s = s[:i] + s[i+1:]
                break
        else:
            return float('inf')
        
        # Move the second to last digit to the second to last position
        for i in range(len(s) - 1, 0, -1):
            if s[i] == s[-2]:
                moves += len(s) - 1 - i
                s = s[:i] + s[i+1:]
                break
        else:
            return float('inf')
        
        # Remove leading zeros
        leading_zeros = 0
        for i in range(len(s)):
            if s[i] == '0':
                leading_zeros += 1
            else:
                break
        
        moves += leading_zeros
        
        return moves
    
    ans = float('inf')
    
    # Check for 00
    s = list(n)
    ans = min(ans, calculate_moves(s[:]))
    
    # Check for 25
    s = list(n)
    s[-1], s[-2] = '5', '2'
    ans = min(ans, calculate_moves(s[:]))
    
    # Check for 50
    s = list(n)
    s[-1], s[-2] = '0', '5'
    ans = min(ans, calculate_moves(s[:]))
    
    # Check for 75
    s = list(n)
    s[-1], s[-2] = '5', '7'
    ans = min(ans, calculate_moves(s[:]))
    
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()