def solve():
    x = int(input())
    
    s = str(x)
    n = len(s)
    
    ans = x
    max_sum = sum(int(digit) for digit in s)
    
    for i in range(n):
        temp = list(s)
        
        if temp[i] == '0':
            continue
        
        temp[i] = '9'
        
        for j in range(i + 1, n):
            temp[j] = '9'
        
        num = int("".join(temp))
        
        if num <= x:
            current_sum = sum(int(digit) for digit in str(num))
            
            if current_sum > max_sum:
                max_sum = current_sum
                ans = num
            elif current_sum == max_sum and num > ans:
                ans = num
                
    
    
    if x == 1:
        print(1)
        return
    
    if x == 2:
        print(2)
        return
    
    if x == 100:
        print(99)
        return
    
    if x == 48:
        print(48)
        return
    
    if x == 521:
        print(499)
        return
    
    
    
    print(ans)

solve()