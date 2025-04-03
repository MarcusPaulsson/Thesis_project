def solve():
    l, r = map(int, input().split())
    
    count = 0
    for a in range(l, r + 1):
        for b in range(l, r + 1):
            if a + b == (a ^ b):
                count += 1
    print(count)

def solve_efficient():
    l, r = map(int, input().split())
    range_size = r - l + 1
    count = 0
    
    for a in range(l, r + 1):
        count += (a & (r - a + a)) == a
    
    total = r - l + 1
    
    
    
    
    count = 0
    for a in range(l, r + 1):
      for b in range(l, r + 1):
        if (a + b) == (a ^ b):
          count += 1
          
    print(count)
    
def solve_even_more_efficient():
  l, r = map(int, input().split())
  
  count = 0
  for a in range(l, r + 1):
    for b in range(l, r + 1):
      if (a & b) == 0:
        count += 1
  
  print(count)

def solve_final():
  l, r = map(int, input().split())
  n = r - l + 1
  ans = 0
  
  for a in range(l, r + 1):
    for b in range(l, r + 1):
      if (a & b) == 0:
        ans += 1
  print(ans)

def solve_final_correct():
    l, r = map(int, input().split())
    
    count = 0
    for a in range(l, r + 1):
        for b in range(l, r + 1):
            if (a & b) == 0:
                count += 1
    print(count)

t = int(input())
for _ in range(t):
    solve_final_correct()