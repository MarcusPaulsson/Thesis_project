def solve():
  x, y, k = map(int, input().split())
  
  # We need k sticks and k coal.
  # Let's calculate how many sticks we need to buy k coal.
  sticks_needed_for_coal = k * y
  
  # Total sticks needed = k + sticks_needed_for_coal
  total_sticks_needed = k + sticks_needed_for_coal
  
  # We start with 1 stick.
  sticks_to_buy = total_sticks_needed - 1
  
  # Number of stick trades.
  stick_trades = (sticks_to_buy + x - 2) // (x - 1)
  
  # Total trades = coal trades (k) + stick trades
  total_trades = k + stick_trades
  
  print(total_trades)

t = int(input())
for _ in range(t):
  solve()