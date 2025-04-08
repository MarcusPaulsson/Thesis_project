def find_midpoint(start_hour, start_minute, end_hour, end_minute):
    # Convert start and end times to total minutes
    start_time = start_hour * 60 + start_minute
    end_time = end_hour * 60 + end_minute
    
    # Calculate midpoint in total minutes
    midpoint_time = (start_time + end_time) // 2
    
    # Convert back to hours and minutes
    midpoint_hour = midpoint_time // 60
    midpoint_minute = midpoint_time % 60
    
    # Format output with leading zeros
    return f"{midpoint_hour:02}:{midpoint_minute:02}"

# Input reading
start_time_input = input().strip()
end_time_input = input().strip()

# Parse input
h1, m1 = map(int, start_time_input.split(':'))
h2, m2 = map(int, end_time_input.split(':'))

# Calculate and print the midpoint
print(find_midpoint(h1, m1, h2, m2))