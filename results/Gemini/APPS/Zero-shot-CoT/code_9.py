def solve():
  s = input()
  groups = []
  i = 0
  while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
      j += 1
    groups.append(s[i])
    i = j
  
  alice_score = 0
  
  while len(groups) > 0:
    max_len = 0
    max_index = -1
    
    curr_len = 1
    for i in range(1, len(groups)):
      if groups[i] == groups[i-1]:
        curr_len+=1
      else:
        if curr_len > max_len:
          max_len = curr_len
          max_index = i-1
        curr_len = 1
    if curr_len > max_len:
        max_len = curr_len
        max_index = len(groups)-1
    
    
    if max_index != -1:
        
        start_index = max_index
        while start_index >= 0 and groups[start_index] == groups[max_index]:
            start_index -= 1
            
        start_index+=1
        
        end_index = max_index
        
        while end_index < len(groups) and groups[end_index] == groups[max_index]:
          end_index+=1
        
        end_index-=1
        
        
        count_ones = 0
        for i in range(start_index, end_index+1):
          if groups[i] == '1':
            count_ones+=1
        
        alice_score+=count_ones
        
        
        new_groups = []
        for i in range(0, start_index):
            new_groups.append(groups[i])
        
        for i in range(end_index+1, len(groups)):
            new_groups.append(groups[i])
            
        groups = new_groups
        
        
        
        
    else:
        count_ones = 0
        for i in range(0, len(groups)):
          if groups[i] == '1':
            count_ones+=1
        
        alice_score+=count_ones
        groups = []
        
        
        
        
        
        
    
    if len(groups) == 0:
        break
    
    
    max_len = 0
    max_index = -1
    
    curr_len = 1
    for i in range(1, len(groups)):
      if groups[i] == groups[i-1]:
        curr_len+=1
      else:
        if curr_len > max_len:
          max_len = curr_len
          max_index = i-1
        curr_len = 1
    if curr_len > max_len:
        max_len = curr_len
        max_index = len(groups)-1
    
    
    if max_index != -1:
        
        start_index = max_index
        while start_index >= 0 and groups[start_index] == groups[max_index]:
            start_index -= 1
            
        start_index+=1
        
        end_index = max_index
        
        while end_index < len(groups) and groups[end_index] == groups[max_index]:
          end_index+=1
        
        end_index-=1
        
        
        
        
        new_groups = []
        for i in range(0, start_index):
            new_groups.append(groups[i])
        
        for i in range(end_index+1, len(groups)):
            new_groups.append(groups[i])
            
        groups = new_groups
        
        
        
        
    else:
        groups = []
    
        
  print(alice_score)
  
t = int(input())
for _ in range(t):
  solve()