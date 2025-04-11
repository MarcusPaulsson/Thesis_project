def solve():
    n = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort()
    x = divisors[-1]
    
    divisors_x = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors_x.append(i)
            if i * i != x:
                divisors_x.append(x // i)
    divisors_x.sort()

    temp_divisors = divisors[:]
    for val in divisors_x:
        if val in temp_divisors:
            temp_divisors.remove(val)

    y = 1
    if len(temp_divisors) > 0:
        y = temp_divisors[-1]
    
    divisors_y = []
    for i in range(1, int(y**0.5) + 1):
        if y % i == 0:
            divisors_y.append(i)
            if i * i != y:
                divisors_y.append(y // i)
    divisors_y.sort()

    merged_divisors = divisors_x + divisors_y
    merged_divisors.sort()
    divisors.sort()

    if merged_divisors == divisors:
        print(x, y)
    else:
        print("Error")

solve()