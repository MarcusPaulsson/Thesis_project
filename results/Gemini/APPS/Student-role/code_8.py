def solve():
  s = input().split()
  
  def check_mentsu(tiles):
    # Check koutsu
    counts = {}
    for tile in tiles:
      if tile not in counts:
        counts[tile] = 0
      counts[tile] += 1
    
    for tile in counts:
      if counts[tile] >= 3:
        return True
    
    # Check shuntsu
    nums = {'m': [], 'p': [], 's': []}
    for tile in tiles:
      nums[tile[1]].append(int(tile[0]))
    
    for suit in ['m', 'p', 's']:
      nums[suit].sort()
      if len(nums[suit]) >= 3:
        for i in range(len(nums[suit]) - 2):
          if nums[suit][i+1] == nums[suit][i] + 1 and nums[suit][i+2] == nums[suit][i] + 2:
            return True
    
    return False
  
  if check_mentsu(s):
    print(0)
    return
  
  # Check if adding one tile can create a mentsu
  for i in range(1, 10):
    for suit in ['m', 'p', 's']:
      new_tile = str(i) + suit
      temp_tiles = s + [new_tile]
      if check_mentsu(temp_tiles):
        print(1)
        return
  
  print(2)
  
solve()