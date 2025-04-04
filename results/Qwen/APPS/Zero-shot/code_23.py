def max_permutation(a, b):
    a = list(str(a))
    b = list(str(b))
    a.sort(reverse=True)
    for i in range(len(a)):
        if a[i] > b[i]:
            for j in range(i, len(a)):
                if a[j] <= b[i]:
                    a[i], a[j] = a[j], a[i]
                    break
        if a[i] < b[i]:
            break
    return int(''.join(a))

a = int(input())
b = int(input())
print(max_permutation(a, b))