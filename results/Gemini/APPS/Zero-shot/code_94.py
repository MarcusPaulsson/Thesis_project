a, b, x = map(int, input().split())

if a > b:
    start = '0'
    a -= 1
else:
    start = '1'
    b -= 1

result = start

for i in range(x - 1):
    if start == '0':
        result += '1'
        start = '1'
        b -= 1
    else:
        result += '0'
        start = '0'
        a -= 1

if start == '0':
    result += '0' * a
    result += '1' * b
else:
    result += '1' * b
    result += '0' * a

print(result)