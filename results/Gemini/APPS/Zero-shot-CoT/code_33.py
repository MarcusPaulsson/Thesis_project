import math

def solve():
    n = int(input())
    nums = list(range(1, n + 1))
    
    for _ in range(n - 2):
        a = nums.pop()
        b = nums.pop()
        new_num = math.ceil((a + b) / 2)
        print(a, b)
        nums.append(new_num)
    
    a = nums.pop()
    b = nums.pop()
    new_num = math.ceil((a + b) / 2)
    print(a, b)
    print(new_num)

t = int(input())
for _ in range(t):
    solve()