h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

# Calculate the total minutes from start to end
total_minutes = (h2 - h1) * 60 + (m2 - m1)

# Calculate the midpoint in minutes
midpoint_minutes = total_minutes // 2

# Calculate the midpoint hour and minute
h3 = h1 + midpoint_minutes // 60
m3 = m1 + midpoint_minutes % 60

# Handle the case where the midpoint minute exceeds 59
if m3 >= 60:
    h3 += 1
    m3 -= 60

# Print the midpoint time in hh:mm format
print(f"{h3:02}:{m3:02}")