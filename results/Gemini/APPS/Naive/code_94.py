def solve():
    a, b, x = map(int, input().split())
    
    if a > b:
        start_with_zero = True
    else:
        start_with_zero = False
    
    result = ""
    
    if start_with_zero:
        if x % 2 == 0:
            while x > 0:
                result += "0"
                a -= 1
                result += "1"
                b -= 1
                x -= 2
            result += "0" * a
            result += "1" * b
        else:
            while x > 1:
                result += "0"
                a -= 1
                result += "1"
                b -= 1
                x -= 2
            result += "0" * a
            result += "1" * b
            result += "0"
            a -= 1
            result = "0" + result
            a -= 1
            result = "0" * a + result
            result = result[1:]
    else:
        if x % 2 == 0:
            while x > 0:
                result += "1"
                b -= 1
                result += "0"
                a -= 1
                x -= 2
            result += "1" * b
            result += "0" * a
        else:
            while x > 1:
                result += "1"
                b -= 1
                result += "0"
                a -= 1
                x -= 2
            result += "1" * b
            result += "0" * a
            result += "1"
            b -= 1
            result = "1" + result
            b -= 1
            result = "1" * b + result
            result = result[1:]

    print(result)

solve()