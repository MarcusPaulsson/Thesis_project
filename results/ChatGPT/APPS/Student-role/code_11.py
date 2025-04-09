n, a, b, p, q = map(int, input().split())

# Calculate the number of tiles painted Red and Blue
red_count = n // a
blue_count = n // b
both_count = n // (a * b)

# Tiles painted Red and not Blue
only_red_count = red_count - both_count
# Tiles painted Blue and not Red
only_blue_count = blue_count - both_count

# Calculate total chocolates
total_chocolates = (only_red_count * p) + (only_blue_count * q) + (both_count * max(p, q))

print(total_chocolates)