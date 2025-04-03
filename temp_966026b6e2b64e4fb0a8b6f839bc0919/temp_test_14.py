def solve():
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    
    if a1 == b1 + b2 and a2 == a1:
        print("Yes")
        return
    if a1 == b1 + a2 and b2 == a1:
        print("Yes")
        return
    if b1 == a1 + b2 and a2 == b1:
        print("Yes")
        return
    if b1 == a1 + a2 and b2 == b1:
        print("Yes")
        return
    
    print("No")

t = int(input())
for _ in range(t):
    solve()