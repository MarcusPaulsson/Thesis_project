def count_exterminable_subarrays(n, a):
    count = 0
    stack = []
    last_position = {}
    
    for i in range(n):
        if stack and stack[-1] == a[i]:
            stack.pop()
        else:
            stack.append(a[i])
        
        if not stack:
            count += (i + 1)
        else:
            last_position[tuple(stack)] = i

        if tuple(stack) in last_position:
            count += last_position[tuple(stack)]

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    q = int(data[index])
    index += 1
    results = []
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        result = count_exterminable_subarrays(n, a)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()