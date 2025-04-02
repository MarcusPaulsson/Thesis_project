def count(a):
    freq = {} # frequency of elements in the array
    for x in a:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
    
    count = 0
    for key, value in freq.items(): # iterate over the frequency dictionary
        if value >= 2: # if an element appears at least twice in the array
            count += value * (value - 1) // 2 # add all pairs of indices with that element
    
    return count // 2 # divide by 2 because of duplicate tuples counted multiple times


# read input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count(a))