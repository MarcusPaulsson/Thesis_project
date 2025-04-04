def longest_increasing_sequence(n, a):
    left = 0
    right = n - 1
    k = 0
    s = ""
    last = -1
    
    while left <= right:
        if a[left] > last and a[left] > a[right]:
            last = a[left]
            s += "L"
            left += 1
        elif a[right] > last and a[right] > a[left]:
            last = a[right]
            s += "R"
            right -= 1
        elif a[left] > last:
            last = a[left]
            s += "L"
            left += 1
        elif a[right] > last:
            last = a[right]
            s += "R"
            right -= 1
        else:
            if a[left] > a[right]:
                s += "L"
                left += 1
            else:
                s += "R"
                right -= 1
        k += 1
    
    return k, s

n = int(input())
a = list(map(int, input().split()))
k, s = longest_increasing_sequence(n, a)
print(k)
print(s)