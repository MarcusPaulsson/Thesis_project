def solve():
    s = input()
    groups = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            groups.append((s[i-1], count))
            count = 1
    groups.append((s[-1], count))
    
    
    while len(groups) > 0:
        
        best_move = -1
        best_move_len = -1
        
        for i in range(len(groups)):
            if groups[i][1] > best_move_len:
                best_move = i
                best_move_len = groups[i][1]
        
        alice_score = 0
        if groups[best_move][0] == '1':
            alice_score = groups[best_move][1]
            
        
        
        
        
        if best_move > 0 and best_move < len(groups) - 1 and groups[best_move - 1][0] == groups[best_move + 1][0]:
            new_count = groups[best_move - 1][1] + groups[best_move + 1][1]
            groups[best_move - 1] = (groups[best_move - 1][0], new_count)
            groups.pop(best_move + 1)
            groups.pop(best_move)
           
        else:
            groups.pop(best_move)
        
        
        
        bob_best_move = -1
        bob_best_move_len = -1
        
        if len(groups) > 0:
            for i in range(len(groups)):
                if groups[i][1] > bob_best_move_len:
                    bob_best_move = i
                    bob_best_move_len = groups[i][1]
                    
            if bob_best_move > 0 and bob_best_move < len(groups) - 1 and groups[bob_best_move - 1][0] == groups[bob_best_move + 1][0]:
                new_count = groups[bob_best_move - 1][1] + groups[bob_best_move + 1][1]
                groups[bob_best_move - 1] = (groups[bob_best_move - 1][0], new_count)
                groups.pop(bob_best_move + 1)
                groups.pop(bob_best_move)
            else:
                groups.pop(bob_best_move)
                
        yield alice_score
    
    

t = int(input())
for _ in range(t):
    ans = sum(solve())
    print(ans)