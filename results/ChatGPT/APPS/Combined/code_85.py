def find_price(A, B):
    for price in range(1, 10001):  # Adjusted upper limit to include 10000
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)
        
        if tax_8 == A and tax_10 == B:
            return price
            
    return -1

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    A, B = map(int, input_data.split())
    result = find_price(A, B)
    print(result)