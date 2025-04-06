from collections import Counter

def solve():
  a = input()
  b = input()
  
  if len(a) < len(b):
    print("".join(sorted(a, reverse=True)))
    return
  
  a_counts = Counter(a)
  
  def find_max(index, current_num, remaining_counts, less):
    if index == len(a):
      return current_num
    
    best_num = ""
    
    possible_digits = sorted(remaining_counts.keys(), reverse=True)
    
    for digit in possible_digits:
      if less or digit <= b[index]:
        new_remaining_counts = remaining_counts.copy()
        new_remaining_counts[digit] -= 1
        if new_remaining_counts[digit] == 0:
          del new_remaining_counts[digit]
          
        new_less = less or (digit < b[index])
        
        res = find_max(index + 1, current_num + digit, new_remaining_counts, new_less)
        
        if res and (not best_num or res > best_num):
          best_num = res
    
    return best_num
  
  print(find_max(0, "", a_counts, False))
  

solve()