def solve():
  s = input()
  
  def calculate_score(moves):
    alice_score = 0
    for i in range(len(moves)):
      if i % 2 == 0:
        alice_score += moves[i]
    return alice_score
  
  def get_moves(current_s):
    moves = []
    i = 0
    while i < len(current_s):
      j = i
      while j < len(current_s) and current_s[i] == current_s[j]:
        j += 1
      moves.append((i, j))
      i = j
    return moves
  
  def play_game(current_s, alice_turn):
    if not current_s:
      return 0
    
    moves = get_moves(current_s)
    best_score = -1
    
    for start, end in moves:
      deleted_ones = 0
      for k in range(start, end):
        if current_s[k] == '1':
          deleted_ones += 1
          
      new_s = current_s[:start] + current_s[end:]
      
      score_after_move = play_game(new_s, not alice_turn)
      
      if alice_turn:
          best_score = max(best_score, deleted_ones + score_after_move if best_score != -1 else deleted_ones + score_after_move)
      else:
          best_score = max(best_score, score_after_move if best_score != -1 else score_after_move)
          
    return best_score
  
  def solve_greedy(s):
      groups = []
      i = 0
      while i < len(s):
          j = i
          while j < len(s) and s[i] == s[j]:
              j += 1
          groups.append(s[i:j])
          i = j
      
      groups.sort(key=len, reverse=True)
      
      alice_score = 0
      for i in range(0, len(groups), 2):
          alice_score += groups[i].count('1')
      
      return alice_score
  
  print(solve_greedy(s))

t = int(input())
for _ in range(t):
  solve()