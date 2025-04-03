def solve():
    n = int(input())
    s = input()
    
    s_list = list(s)
    
    moves = []
    
    i = 0
    while i < len(s_list) - 1:
        if s_list[i] == '1' and s_list[i+1] == '0':
            moves.append(i)
        i += 1
    
    while moves:
        idx = moves.pop(0)
        
        
        temp_s_list1 = s_list[:idx] + s_list[idx+1:]
        temp_s_list2 = s_list[:idx+1] + s_list[idx+2:]
                
        
        s_list = min(temp_s_list1, temp_s_list2, key=lambda x: (len(x), x))
        
        moves = []
        i = 0
        while i < len(s_list) - 1:
            if s_list[i] == '1' and s_list[i+1] == '0':
                moves.append(i)
            i += 1
    
    print("".join(s_list))

t = int(input())
for _ in range(t):
    solve()