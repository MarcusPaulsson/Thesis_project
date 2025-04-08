def moves_to_transform(n, m):
    if m % n != 0:
        return -1
    
    factor = m // n
    count_2 = 0
    count_3 = 0
    
    while factor % 2 == 0:
        factor //= 2
        count_2 += 1
    
    while factor % 3 == 0:
        factor //= 3
        count_3 += 1
    
    return count_2 + count_3 if factor == 1 else -1

def main():
    n, m = map(int, input().split())
    print(moves_to_transform(n, m))

if __name__ == "__main__":
    main()