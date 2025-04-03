def solve():
    n = int(input())
    s = input()
    
    def get_operations(s):
        if not s:
            return 0
        
        max_ops = 0
        for i in range(len(s)):
            temp_s = list(s)
            del temp_s[i]
            temp_s = "".join(temp_s)
            
            if not temp_s:
                max_ops = max(max_ops, 1)
                continue
                
            first_char = temp_s[0]
            prefix_len = 0
            for j in range(len(temp_s)):
                if temp_s[j] == first_char:
                    prefix_len += 1
                else:
                    break
            
            temp_s = temp_s[prefix_len:]
            
            max_ops = max(max_ops, 1 + get_operations(temp_s))
        
        return max_ops

    print(get_operations(s))
    

t = int(input())
for _ in range(t):
    solve()