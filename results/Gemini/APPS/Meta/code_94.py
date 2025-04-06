def solve():
    a, b, x = map(int, input().split())

    def construct_string(start_with_one):
        s = ""
        if start_with_one:
            s += "1"
            b -= 1
        else:
            s += "0"
            a -= 1
        
        switches = 0
        last_digit = s[-1]
        
        while a > 0 or b > 0:
            if last_digit == '0':
                if b > 0 and switches < x:
                    s += '1'
                    b -= 1
                    switches += 1
                    last_digit = '1'
                else:
                    s += '0'
                    a -= 1
                    last_digit = '0'
            else:
                if a > 0 and switches < x:
                    s += '0'
                    a -= 1
                    switches += 1
                    last_digit = '0'
                else:
                    s += '1'
                    b -= 1
                    last_digit = '1'
        return s

    if a > b:
        ans = construct_string(False)
    else:
        ans = construct_string(True)

    count = 0
    for i in range(len(ans) - 1):
        if ans[i] != ans[i+1]:
            count += 1
    
    print(ans)

solve()