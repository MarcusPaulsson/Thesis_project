def solve():
    n = int(input())
    s = input()
    target = "abacaba"
    
    def check(modified_s):
        count = 0
        for i in range(len(modified_s) - len(target) + 1):
            if modified_s[i:i+len(target)] == target:
                count += 1
        return count
    
    for i in range(n - len(target) + 1):
        temp_s = list(s)
        possible = True
        for j in range(len(target)):
            if temp_s[i+j] == '?':
                temp_s[i+j] = target[j]
            elif temp_s[i+j] != target[j]:
                possible = False
                break
        
        if possible:
            modified_s = "".join(temp_s)
            
            final_s = list(modified_s)
            for k in range(len(final_s)):
                if final_s[k] == '?':
                    final_s[k] = 'd'
            final_s = "".join(final_s)
            
            if check(final_s) == 1:
                print("Yes")
                print(final_s)
                return
    
    print("No")

t = int(input())
for _ in range(t):
    solve()