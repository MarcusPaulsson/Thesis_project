def solve():
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    unlocked_indices = [i for i in range(n) if l[i] == 0]
    unlocked_values = [a[i] for i in unlocked_indices]
    unlocked_values.sort()
    
    new_a = a[:]
    
    for i in range(len(unlocked_indices)):
        new_a[unlocked_indices[i]] = unlocked_values[i]
        
    print(*new_a)

t = int(input())
for _ in range(t):
    solve()