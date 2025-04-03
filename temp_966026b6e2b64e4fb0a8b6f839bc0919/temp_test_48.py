def solve():
  x, y, k = map(int, input().split())
  
  # Need k sticks and k coal
  # k coal require k * y sticks
  # Total sticks needed: k + k * y
  # We start with 1 stick
  # We need to buy k + k * y - 1 sticks
  # Each trade gives us x - 1 sticks
  
  sticks_needed = k + k * y - 1
  trades_sticks = (sticks_needed + x - 2) // (x - 1)
  
  print(trades_sticks + k)
  

t = int(input())
for _ in range(t):
  solve()