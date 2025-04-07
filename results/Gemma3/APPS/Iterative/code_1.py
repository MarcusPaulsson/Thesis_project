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
        
        temp[i] = str(int(temp[i]) - 1)
        
        for j in range(i + 1, n):
            temp[j] = '9'
        
        num = int("".join(temp))
        
        if num > 0:
            current_sum = sum(int(digit) for digit in str(num))
            
            if current_sum > max_sum:
                max_sum = current_sum
                ans = num
            elif current_sum == max_sum and num > ans:
                ans = num
                
    
    
    
    
    
    print(ans)

solve()