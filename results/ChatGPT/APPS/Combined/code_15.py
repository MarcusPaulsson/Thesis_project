def will_number_appear(a, b, c):
    if c == 0:
        return "YES" if a == b else "NO"
    
    difference = b - a
    if difference % c == 0 and difference // c >= 0:
        return "YES"
    
    return "NO"

# Read input
a, b, c = map(int, input().split())
# Output result
print(will_number_appear(a, b, c))