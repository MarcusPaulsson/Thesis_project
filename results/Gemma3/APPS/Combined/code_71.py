def solve():
    a = int(input())
    
    if a == 1:
        print(1)
        return
    
    print(a.bit_length() - 1)

solve()