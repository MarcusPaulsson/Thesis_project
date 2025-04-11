def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    odd_count = 0
    even_count = 0
    for val in x:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print(min(odd_count, even_count))

solve()