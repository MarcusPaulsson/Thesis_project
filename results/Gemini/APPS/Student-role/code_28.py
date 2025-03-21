def solve():
    n = int(input())
    s = input()
    target = "abacaba"
    
    def check(t):
        count = 0
        for i in range(len(t) - 6):
            if t[i:i+7] == target:
                count += 1
        return count
    
    def replace_all(t):
        return t.replace('?', 'd')
    
    for i in range(n - 6):
        temp = list(s)
        possible = True
        for j in range(7):
            if temp[i+j] == '?':
                temp[i+j] = target[j]
            elif temp[i+j] != target[j]:
                possible = False
                break
        
        if possible:
            temp_str = "".join(temp)
            
            
            
            
            temp_str = replace_all(temp_str)
            
            
            if check(temp_str) == 1:
                print("Yes")
                print(temp_str)
                return
    
    print("No")

t = int(input())
for _ in range(t):
    solve()