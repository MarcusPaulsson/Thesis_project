def count_good_substrings(s):
    n = len(s)
    good_count = 0
    
    for l in range(n):
        # Initialize the number represented by the substring as 0
        num = 0
        
        for r in range(l, n):
            # Update the number based on the current character
            num = num * 2 + int(s[r])
            length = r - l + 1
            
            # Check if the substring is good
            if length == num:
                good_count += 1
                
    return good_count

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        results.append(count_good_substrings(s))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()