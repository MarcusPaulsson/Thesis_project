def solve():
    s = input()
    n = len(s)
    ans = -1
    for i in range(n):
        for j in range(i + 3, n):
            if s[i] == '[' and s[j] == ']':
                
                first_colon_index = -1
                for k in range(i + 1, j):
                    if s[k] == ':':
                        first_colon_index = k
                        break
                
                if first_colon_index == -1:
                    continue
                    
                second_colon_index = -1
                for k in range(first_colon_index + 1, j):
                    if s[k] == ':':
                        second_colon_index = k
                        break
                        
                if second_colon_index == -1:
                    continue
                    
                vertical_bars_count = 0
                for k in range(first_colon_index + 1, second_colon_index):
                    if s[k] == '|':
                        vertical_bars_count += 1
                    else:
                        vertical_bars_count = -1000
                        break
                        
                if vertical_bars_count >= 0:
                    ans = max(ans, 4 + vertical_bars_count)
                    
    print(ans)

solve()