h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

# Convert start and end times to total minutes
start_minutes = h1 * 60 + m1
end_minutes = h2 * 60 + m2

# Calculate the midpoint in total minutes
midpoint_minutes = (start_minutes + end_minutes) // 2

# Convert back to hours and minutes
h3 = midpoint_minutes // 60
m3 = midpoint_minutes % 60

# Print the result in the required format
print(f"{h3:02}:{m3:02}")