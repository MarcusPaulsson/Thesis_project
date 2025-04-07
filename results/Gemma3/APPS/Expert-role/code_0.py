def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            
            if len(sub) < 4:
                continue
            
            if sub[0] != '[' or sub[-1] != ']':
                continue
            
            colon_count = 0
            for k in range(len(sub)):
                if sub[k] == ':':
                    colon_count += 1
            
            if colon_count != 2:
                continue
            
            first_colon = -1
            second_colon = -1
            
            for k in range(len(sub)):
                if sub[k] == ':' and first_colon == -1:
                    first_colon = k
                elif sub[k] == ':' and second_colon == -1:
                    second_colon = k
            
            if first_colon == -1 or second_colon == -1 or first_colon >= second_colon:
                continue
            
            valid = True
            for k in range(first_colon + 1, second_colon):
                if sub[k] != '|':
                    valid = False
                    break
            
            if not valid:
                continue
            
            max_len = max(max_len, len(sub))
            
    print(max_len)

solve()