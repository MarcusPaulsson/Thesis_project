def solve():
    s = input()
    
    def calculate_score(moves):
        alice_score = 0
        for i in range(0, len(moves), 2):
            alice_score += moves[i]
        return alice_score
    
    def get_possible_moves(current_s):
        moves = []
        i = 0
        while i < len(current_s):
            j = i
            while j < len(current_s) and current_s[i] == current_s[j]:
                j += 1
            moves.append((i, j))
            i = j
        return moves

    def play_game(current_s, alice_turn, alice_score, bob_score):
        if not current_s:
            return alice_score
        
        possible_moves = get_possible_moves(current_s)
        
        best_score = -1 if alice_turn else float('inf')
        
        for start, end in possible_moves:
            deleted_ones = 0
            for k in range(start, end):
                if current_s[k] == '1':
                    deleted_ones += 1
                    
            new_s = current_s[:start] + current_s[end:]
            
            if alice_turn:
                new_alice_score = alice_score + deleted_ones
                score = play_game(new_s, False, new_alice_score, bob_score)
                best_score = max(best_score, score)
            else:
                new_bob_score = bob_score + deleted_ones
                score = play_game(new_s, True, alice_score, new_bob_score)
                best_score = min(best_score, score)
                
        return best_score

    def solve_greedy(s):
      groups = []
      i = 0
      while i < len(s):
        j = i
        while j < len(s) and s[i] == s[j]:
          j+=1
        groups.append(s[i])
        i = j
      
      groups.sort()
      
      ones = 0
      for char in groups:
        if char == '1':
          ones += 1
      
      return (ones + 1) // 2
    
    s = s.strip()
    
    grouped = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[i] == s[j]:
            j += 1
        grouped.append(s[i:j])
        i = j
    
    ones = 0
    for group in grouped:
      ones += group.count('1')

    
    grouped.sort(key=len, reverse=True)

    alice_score = 0
    turn = True
    while grouped:
        best_group = -1
        best_group_index = -1
        for i in range(len(grouped)):
            group = grouped[i]
            score = group.count('1')
            if best_group == -1 or score > best_group:
                best_group = score
                best_group_index = i

        if turn:
            alice_score += best_group
        
        grouped.pop(best_group_index)
        turn = not turn
    
    print( solve_greedy(s))
    

t = int(input())
for _ in range(t):
    solve()