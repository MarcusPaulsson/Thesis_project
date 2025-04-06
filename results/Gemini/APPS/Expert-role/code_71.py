def solve():
    a = int(input())
    
    count = 0
    curr = 1
    while curr <= a:
        curr *= 2
        count += 1
    
    print(count - 1)

solve()