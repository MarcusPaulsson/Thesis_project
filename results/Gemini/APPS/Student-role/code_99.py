def solve():
  n = int(input())
  a1, a2, a3 = map(int, input().split())
  b1, b2, b3 = map(int, input().split())

  min_wins = 0
  
  # Calculate minimum wins
  temp_a1, temp_a2, temp_a3 = a1, a2, a3
  temp_b1, temp_b2, temp_b3 = b1, b2, b3

  # Minimize wins by maximizing losses
  
  # Alice rock vs Bob rock
  take = min(temp_a1, temp_b1)
  temp_a1 -= take
  temp_b1 -= take
  
  # Alice rock vs Bob scissors
  
  # Alice rock vs Bob paper
  take = min(temp_a1, temp_b3)
  temp_a1 -= take
  temp_b3 -= take

  # Alice scissors vs Bob rock
  take = min(temp_a2, temp_b1)
  temp_a2 -= take
  temp_b1 -= take

  # Alice scissors vs Bob scissors
  
  # Alice scissors vs Bob paper
  take = min(temp_a2, temp_b2)
  temp_a2 -= take
  temp_b2 -= take
  

  # Alice paper vs Bob rock
  take = min(temp_a3, temp_b1)
  temp_a3 -= take
  temp_b1 -= take
  
  # Alice paper vs Bob scissors
  take = min(temp_a3, temp_b2)
  temp_a3 -= take
  temp_b2 -= take
  
  # Alice paper vs Bob paper
  take = min(temp_a3, temp_b3)
  temp_a3 -= take
  temp_b3 -= take
  
  min_wins = max(0, a1 - (n - temp_a1 -temp_a2 - temp_a3))
  
  # Calculate maximum wins
  max_wins = 0
  
  # Alice rock vs Bob scissors
  take = min(a1, b2)
  max_wins += take
  a1 -= take
  b2 -= take
  
  # Alice scissors vs Bob paper
  take = min(a2, b3)
  max_wins += take
  a2 -= take
  b3 -= take
  
  # Alice paper vs Bob rock
  take = min(a3, b1)
  max_wins += take
  a3 -= take
  b1 -= take

  print(min_wins, max_wins)

solve()