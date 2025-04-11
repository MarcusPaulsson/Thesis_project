def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    for d in range(101):
        possible = True
        
        
        first_val = None
        
        
        for target in range(1, 101):
            
            valid_d = True
            
            
            first_val_found = False
            
            for i in range(n):
                
                if a[i] == target:
                    if not first_val_found:
                        first_val_found = True
                    continue
                elif a[i] + d == target:
                    if not first_val_found:
                        first_val_found = True
                    continue
                elif a[i] - d == target:
                    if not first_val_found:
                        first_val_found = True
                    continue
                else:
                    valid_d = False
                    break
            
            if valid_d and first_val_found:
                print(d)
                return
    
    print(-1)

solve()