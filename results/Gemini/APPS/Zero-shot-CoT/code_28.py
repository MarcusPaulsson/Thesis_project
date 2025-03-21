def solve():
    n = int(input())
    s = input()
    target = "abacaba"
    
    def check(modified_s):
        count = 0
        for i in range(n - 6):
            if modified_s[i:i+7] == target:
                count += 1
        return count
    
    def replace_all(modified_s):
        result = ""
        for char in modified_s:
            if char == '?':
                result += 'd'
            else:
                result += char
        return result
    
    for i in range(n - 6):
        temp_s = list(s)
        possible = True
        for j in range(7):
            if temp_s[i+j] == '?':
                temp_s[i+j] = target[j]
            elif temp_s[i+j] != target[j]:
                possible = False
                break
        
        if possible:
            modified_s = "".join(temp_s)
            
            final_s = replace_all(modified_s)
            
            if check(final_s) == 1:
                print("Yes")
                print(final_s)
                return
    
    print("No")

t = int(input())
for _ in range(t):
    solve()